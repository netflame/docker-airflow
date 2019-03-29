# docker-airflow

### how to use
0. ```docker pull netflame/airflow``` （or you can build yourself）
1. customize ***.env*** that you need
2. ```docker-compose up -d``` (perhaps you need modify docker-compose.yml to to suit your .env)

### attention
ensure **airflow** start behind **mysql**