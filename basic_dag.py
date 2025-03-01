from airflow import DAG
from airflow.operators.bash import BashOperator
from airlfow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default argumetns for the DAG
default_args = {
    'owner' : 'airflow',
    'start_date' : datetime(2023, 11, 1),
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
}

# Define the DAG
