FROM python:3.6.7-alpine3.8

LABEL maintainer=ilpan:<pna.dev@outlook.com>

ENV AIRFLOW_GPL_UNIDECODE=yes
ARG extra_packages="celery,mysql,password"

RUN apk update \
    && apk add --no-cache \
        curl \
        libstdc++ \
        mariadb-dev \
    && apk add --no-cache --virtual .build-deps \
        g++ \
        libffi-dev \
        libressl-dev \
        libxml2-dev \
        libxslt-dev \
        linux-headers \
    && pip install -U --no-cache-dir pip \
    && pip install --no-cache-dir cython numpy redis

RUN pip install --no-cache-dir apache-airflow[${extra_packages}] \
    && apk del .build-deps \
    && pip uninstall -y cython


ENV AIRFLOW_HOME=/airflow
ENV AIRFLOW__CORE__DAGS_FOLDER=${AIRFLOW_HOME}/dags \
    AIRFLOW__CORE__BASE_LOG_FLODER=${AIRFLOW_HOME}/logs \
    AIRFLOW__CORE__DEFAULT_TIMEZONE=utc \
    AIRFLOW__CORE__EXECUTOR=SequentialExecutor \
    AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////${AIRFLOW_HOME}/airflow.db \
    AIRFLOW__CORE__LOAD_EXAMPLES=False \
    AIRFLOW__WEBSERVER__WEB_SERVER_PORT=8080 \
    AIRFLOW__WEBSERVER__AUTHENTICATE=True \
    AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth \
    AIRFLOW__WEBSERVER__DAG_DEFAULT_VIEW=tree

WORKDIR ${AIRFLOW_HOME}

COPY ./create_user.py ./
COPY ./docker-entrypoint.sh ./

EXPOSE 8080

ENTRYPOINT [ "./docker-entrypoint.sh" ]
