#!/usr/bin/env sh

airflow resetdb -y \
    && airflow initdb \
    && python create_user.py \
    && touch webserver.out scheduler.out
nohup airflow webserver >> webserver.out &
nohup airflow scheduler >> scheduler.out &
tail -f webserver.out scheduler.out