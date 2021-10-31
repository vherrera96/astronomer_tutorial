from airflow import DAG
from airflow.operators.dummy import DummyOperator

from datetime import datetime

with DAG(dag_id = 'simple_dag', start_date = datetime(2021, 1, 1)) as dag:
    DummyOperator(task_id = 'task_1')