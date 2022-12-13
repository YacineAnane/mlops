#datetime
from datetime import timedelta, datetime

# The DAG object
from airflow import DAG

# Operators
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


import pandas as pd
import numpy as np
from eurybia import SmartDrift

default_args = {
		'owner': 'Charli',
		'start_date': datetime(2022, 12, 10),
		'retries': 3,
		'retry_delay': timedelta(minutes=5)
}
'''
hello_world_dag = DAG('hello_world_dag',
		default_args=default_args,
		description='Hello World DAG',
		schedule_interval='* * * * *', 
		catchup=False,
		tags=['example, helloworld']
)

def print_hello():
		return 'Hello World!'

start_task = DummyOperator(task_id='start_task', dag=hello_world_dag):

hello_world_task = PythonOperator(task_id='hello_world_task', python_callable=print_hello, dag=hello_world_dag)

end_task = DummyOperator(task_id='end_task', dag=hello_world_dag)

start_task >> hello_world_task >> end_task
'''



def check_data_drift(output_file="report.html", title="Data drift report"):
  sd = SmartDrift(
    pd.read_csv('~/Bureau/mlops/data/random_data.csv'),
    pd.read_csv('~/Bureau/mlops/data/train.csv'),
    # deployed_model=model, # Optional: put in perspective result with importance on deployed model
    dataset_names={"df_current": "Production dataset", "df_baseline": "Trainning dataset"} # Optional: Names for outputs
    )

  sd.compile()

  sd.generate_report(
    output_file=output_file,
    title_story=title
    )

default_args = {
		'owner': 'Charli',
		'start_date': datetime(2022, 12, 10),
		'retries': 3,
		'retry_delay': timedelta(minutes=5)
}
data_drift_dag = DAG('data_drift_dag',
		default_args=default_args,
		description='DAG for datadrift',
		schedule_interval='* * * * *', 
)

data_drift_task = PythonOperator(task_id='data_drift_task', python_callable=check_data_drift, dag=data_drift_dag)

end_task = DummyOperator(task_id='end_task', dag=data_drift_dag)
data_drift_task >> end_task
