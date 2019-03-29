#!/usr/bin/env sh

scrapyd_host=scrapyd
scrapyd_port=6800
project_name=wscrape

function help() {
    echo "Help on schedule (spider to run)"
    echo "==================="
    echo "options:"
    echo "  -H:    scrapyd host (default is 'scrapyd')"
    echo "  -P:    scrapyd port (default is 6800)"
    echo "  -p:    project name (default is wscrape)"
    echo "  -s:    spider name ['site', edu_{site}, ent_{site}, finance_{site}, tech_{site}, world_{site}]"
    echo "         available sites are 'netease','sohu','tencent','toutiao'"
    echo ""
}

if [ $# -eq 0 ]; then
    help
    exit 1
fi

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
    echo "spider name can't be empty, add it by -s 'spider_name'"
    echo ""
    exit 1
fi

schedule_api=http://${scrapyd_host}:${scrapyd_port}/schedule.json

curl $schedule_api -d project=${project_name} -d spider=${spider_name}
