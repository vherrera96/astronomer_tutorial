from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, time, timedelta

def _downloading_data(my_parameter):
     print(my_parameter)

with DAG(dag_id = 'simple_dag', schedule_interval = "@daily", 
         start_date = days_ago(3), catchup = False) as dag:
    downloading_data = PythonOperator(task_id = 'downloading_data', 
                                      python_callable = _downloading_data,
                                      op_kwargs = {'my_parameter': 42})