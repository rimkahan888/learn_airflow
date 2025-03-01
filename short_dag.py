from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

args = (
    'owner' : 'me',
    'start_date' : datetime(2023,1,1),
    'retries' : 1
    'retry_delay' : timedelta(minutes =1),
}

with DAG(
    'simple_dag',
    default_args = args,
    description='Simple DAG',
    schedule_interval =timedelta(days=1),
    catchup=False,
) as DAG: 


    t1 =BashOperator(
        task_id='t1',
        bash_command = 'echo "hello"'
    )
  
    def fn():
        print("hi")

    t2 =PythonOperator(
        task_id='t2',
        python_command = fn  
    )

    t3=BashOperator(
        task_id ='t3',
        bash_command = 'echo " finish job"
    )

    t1 >> t2 >> t3
