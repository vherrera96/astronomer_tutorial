from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from datetime import datetime, time, timedelta

def _downloading_data(my_parameter):
     with open('/tmp/my_file.txt', 'w') as f:
          f.write('my_data')

with DAG(dag_id = 'simple_dag', schedule_interval = "@daily", 
         start_date = days_ago(3), catchup = False) as dag:
    downloading_data = PythonOperator(task_id = 'downloading_data', 
                                      python_callable = _downloading_data,
                                      op_kwargs = {'my_parameter': 42})
    waiting_for_data = FileSensor(task_id = 'waiting_for_data',
                                  fs_conn_id = 'fs_default',
                                  filepath = 'my_file.txt')