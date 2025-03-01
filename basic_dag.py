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
with DAG(
    'basic_example_dag',                    # DAG ID 
    default_args=default_args,
    description='A Simple Airflow DAG',        # Run daily (@daily)
    schedule_interval=timedelta(days=1),        # Skip historical runs
    catchup=False,
) as dag:

    #Task 1: Print "Hello, World'! using Bash
    task_hello_bash=BashOperator(
        task_id='hello_bash'
        bash_command='echo "Hello, World from Bash!"'

    #Task 2: Print "Hello from Python!" using Python
    def print_hello_python():
        print("Hello from Python!)

    task_hello_python = PythonOperator(
        task_id ='hello_python',
        python_callable = print_hello_python

    PythonOperator
    BashOperator

    
    
