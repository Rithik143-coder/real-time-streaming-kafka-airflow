from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('retail_order_processing',
          default_args=default_args,
          schedule_interval='@daily',
          catchup=False)

process_data = BashOperator(
    task_id='process_data_with_spark',
    bash_command='spark-submit /path/to/spark_job.py',
    dag=dag
)
