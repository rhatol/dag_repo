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

run_data_prep = BashOperator(
    task_id='run_data_prep',
    bash_command='echo "PREPARING DATA....."',
    dag=dag,
)

run_train_data = BashOperator(
    task_id='run_train_aata',
    bash_command='echo "TRAINING DATA....."',
    dag=dag,
)

run_score_data = BashOperator(
    task_id='run_score_data',
    bash_command='echo "SCORE DATA....."',
    dag=dag,
)

run_deploy_model = BashOperator(
    task_id='run_deploy_data',
    bash_command='echo "DEPLOYING MODEL....."',
    dag=dag,
)

run_get_data >> run_data_prep >> run_train_data >> run_score_data >> run_deploy_model
    
if __name__ == "__main__":
    dag.cli()
    
    




