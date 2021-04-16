from builtins import range
from datetime import timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'Airflow',
    'start_date': days_ago(2),
}

dag = DAG(
    dag_id='example_workflow',
    default_args=args,
    schedule_interval='0 0 * * *',
    dagrun_timeout=timedelta(minutes=60),
    tags=['sample_workflow']
)

run_init = DummyOperator(
    task_id='run_init',
    dag=dag,
)

run_get_data = BashOperator(
    task_id='run_get_data',
    bash_command='echo "GETTING DATA FROM SOURCE....."',
    dag=dag,
)

run_init >> run_get_data
