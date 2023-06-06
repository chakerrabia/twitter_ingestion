from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_airflow_installation',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Hello, Airflow!"',
    dag=dag
)

task2 = BashOperator(
    task_id='task2',
    bash_command='echo "Airflow is working!"',
    dag=dag
)

task1 >> task2
