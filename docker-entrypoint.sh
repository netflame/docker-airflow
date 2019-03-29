#!/usr/bin/env sh

airflow resetdb -y \
    && airflow initdb \
    && python create_user.py \
    && mkdir -p out && touch out/webserver.out out/scheduler.out
nohup airflow webserver >> out/webserver.out &
nohup airflow scheduler >> out/scheduler.out &

if (( $# -ge 1 )); then
    for subcmd in $@
    do
        flag=0
        case $subcmd in
            worker)
            flag=1
            ;;
            flower)
            flag=1
            ;;
            *)
            ;;
        esac
        if [ $flag == 1 ]; then
            nohup airflow $subcmd >> out/${subcmd}.out &
        fi
    done
fi

tail -f out/*