from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import cross_downstream

from datetime import datetime, time, timedelta

def _downloading_data(my_parameter):
     with open('/tmp/my_file.txt', 'w') as f:
          f.write('my_data')

def _checking_data():
     print('Checking data')

with DAG(dag_id = 'simple_dag', schedule_interval = "@daily", 
         start_date = days_ago(3), catchup = False) as dag:
    downloading_data = PythonOperator(task_id = 'downloading_data', 
                                      python_callable = _downloading_data,
                                      op_kwargs = {'my_parameter': 42})
    
    checking_data = PythonOperator(task_id = 'checking_data',
                                   python_callable = _checking_data,
                                   )
    
    waiting_for_data = FileSensor(task_id = 'waiting_for_data',
                                  fs_conn_id = 'fs_default',
                                  filepath = 'my_file.txt')
    processing_data = BashOperator(task_id = 'processing_data',
                                   bash_command = 'exit 0')
    
    cross_downstream([downloading_data, checking_data], [waiting_for_data, processing_data])