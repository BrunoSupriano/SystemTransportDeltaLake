from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def ingest_data():
    # Aqui você implementa a lógica para ingestão de dados
    print("Ingestão de dados realizada com sucesso!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 15),
}

with DAG('my_data_pipeline', 
         schedule_interval='@daily', 
         default_args=default_args, 
         catchup=False) as dag:

    ingest_task = PythonOperator(
        task_id='ingest_data_task',
        python_callable=ingest_data,
    )

