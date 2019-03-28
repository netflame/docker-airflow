#!/usr/bin/env python
# -*- coding: utf-8 -*-

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from os import getenv

schedule = '{0}/{1}/schedule.sh'.format(getenv('AIRFLOW_HOME'), 'bin')

default_args = {
    'owner': 'netflame',
    'depends_on_past': False,
    'start_date': datetime(2018, 3, 30),
    'email': ['netflame@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# instantiate a DAG
dag = DAG(
    dag_id='wscrape',
    description='crawl news from specific sites',
    schedule_interval='0 0 * * *',
    default_args=default_args
)

# Tasks
# 0. task_wscrape
task_wscrape = DummyOperator(task_id='wscrape', dag=dag)

# 1. task_edu
task_edu = DummyOperator(task_id='edu', dag=dag)
task_edu_netease = BashOperator(
    task_id='edu_netease',
    bash_command='{0} -s edu_netease'.format(schedule),
    dag=dag
)
task_edu_sohu = BashOperator(
    task_id='edu_sohu',
    bash_command='{0} -s edu_sohu'.format(schedule),
    dag=dag
)
task_edu_tencent = BashOperator(
    task_id='edu_tencent',
    bash_command='{0} -s edu_tencent'.format(schedule),
    dag=dag
)
task_edu_toutiao = BashOperator(
    task_id='edu_toutiao',
    bash_command='{0} -s edu_toutiao'.format(schedule),
    dag=dag 
)

task_edu.set_downstream([task_edu_netease, task_edu_sohu, 
        task_edu_tencent, task_edu_toutiao])

# 2. task_ent
task_ent = DummyOperator(task_id='ent', dag=dag)
task_ent_netease = BashOperator(
    task_id='ent_netease',
    bash_command='{0} -s ent_netease'.format(schedule),
    dag=dag
)
task_ent_sohu = BashOperator(
    task_id='ent_sohu',
    bash_command='{0} -s ent_sohu'.format(schedule),
    dag=dag
)
task_ent_tencent = BashOperator(
    task_id='ent_tencent',
    bash_command='{0} -s ent_tencent'.format(schedule),
    dag=dag
)
task_ent_toutiao = BashOperator(
    task_id='ent_toutiao',
    bash_command='{0} -s ent_toutiao'.format(schedule),
    dag=dag 
)

task_ent.set_downstream([task_ent_netease, task_ent_sohu, 
        task_ent_tencent, task_ent_toutiao])

# 3. task_finance
task_finance = DummyOperator(task_id='finance', dag=dag)
task_finance_netease = BashOperator(
    task_id='finance_netease',
    bash_command='{0} -s finance_netease'.format(schedule),
    dag=dag
)
task_finance_sohu = BashOperator(
    task_id='finance_sohu',
    bash_command='{0} -s finance_sohu'.format(schedule),
    dag=dag
)
task_finance_tencent = BashOperator(
    task_id='finance_tencent',
    bash_command='{0} -s finance_tencent'.format(schedule),
    dag=dag
)
task_finance_toutiao = BashOperator(
    task_id='finance_toutiao',
    bash_command='{0} -s finance_toutiao'.format(schedule),
    dag=dag 
)

task_finance.set_downstream([task_finance_netease, task_finance_sohu,
        task_finance_tencent, task_finance_toutiao])

# 4. task_tech
task_tech = DummyOperator(task_id='tech', dag=dag)
task_tech_netease = BashOperator(
    task_id='tech_netease',
    bash_command='{0} -s tech_netease'.format(schedule),
    dag=dag
)
task_tech_sohu = BashOperator(
    task_id='tech_sohu',
    bash_command='{0} -s tech_sohu'.format(schedule),
    dag=dag
)
task_tech_tencent = BashOperator(
    task_id='tech_tencent',
    bash_command='{0} -s tech_tencent'.format(schedule),
    dag=dag
)
task_tech_toutiao = BashOperator(
    task_id='tech_toutiao',
    bash_command='{0} -s tech_toutiao'.format(schedule),
    dag=dag 
)

task_tech.set_downstream([task_tech_netease, task_tech_sohu,
        task_tech_tencent, task_tech_toutiao])

# 5. task_world
task_world = DummyOperator(task_id='world', dag=dag)
task_world_netease = BashOperator(
    task_id='world_netease',
    bash_command='{0} -s world_netease'.format(schedule),
    dag=dag
)
task_world_sohu = BashOperator(
    task_id='world_sohu',
    bash_command='{0} -s world_sohu'.format(schedule),
    dag=dag
)
task_world_tencent = BashOperator(
    task_id='world_tencent',
    bash_command='{0} -s world_tencent'.format(schedule),
    dag=dag
)
task_world_toutiao = BashOperator(
    task_id='world_toutiao',
    bash_command='{0} -s world_toutiao'.format(schedule),
    dag=dag 
)

task_world.set_downstream([task_world_netease, task_world_sohu,
        task_world_tencent, task_world_toutiao])

# setting up dependencies
task_wscrape >> [task_edu, task_ent, task_finance, task_tech, task_world]

