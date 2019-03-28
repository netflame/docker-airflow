#!/usr/bin/env sh

scrapyd_host=scrapyd
scrapyd_port=6800
project_name=wscrape

while getopts ":H:P:p:s:" opt
do
    case "$opt" in
        H)
            scrapyd_host=$OPTARG
        ;;
        P)
            scrapyd_port=$OPTARG
        ;;
        p)
            project_name=$OPTARG
        ;;
        s)
            spider_name=$OPTARG
        ;;
        *)
        ;;
    esac
done

if [ ! -n "$spider_name" ]; then
    echo "spider name can't be empty"
    echo "add it by -s 'spider_name'"
    exit 1
fi

schedule_api=http://${scrapyd_host}:${scrapyd_port}/schedule.json

curl $schedule_api -d project=${project_name} -d spider=${spider_name}
