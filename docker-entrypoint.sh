#!/usr/bin/env sh

airflow resetdb -y \
    && airflow initdb \
    && python create_user.py \
    && touch webserver.out scheduler.out
nohup airflow webserver >> webserver.out &
nohup airflow scheduler >> scheduler.out &

if (( $# >= 1 )); then
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
            nohup airflow $subcmd >> ${subcmd}.out &
        fi
    done
fi

tail -f webserver.out scheduler.out