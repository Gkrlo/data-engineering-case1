from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
from datetime import datetime, timedelta
import os

args = {'owner':'airflow',
        'start_date': datetime(2020, 3, 25),
        'retries': 1,
        'retry_delay': timedelta(minutes=10)}

dag = DAG(dag_id='aplazame_etls',
          default_args = args,
          catchup = False)


spark_submit = ("$SPARK_HOME/bin/spark-submit --master spark://10.0.0.31:7077 --executor-memory 1G --num-executors 2 " +
    "--driver-class-path /opt/aplazame_jars/postgresql-42.2.12.jar --jars /opt/aplazame_jars/postgresql-42.2.12.jar " + 
    "--conf spark.executor.extraClassPath=/opt/aplazame_jars/postgresql-42.2.12.jar $AIRFLOW_HOME/dags/aplazame_etls/summaries.py")

with dag:
        create_schema = BashOperator(
                task_id='create_schema', 
                bash_command="export PYTHONPATH=$AIRFLOW_HOME/dags:$PYTHONPATH; python3 $AIRFLOW_HOME/dags/aplazame_etls/create_schema.py")

        stage_tables = BashOperator(
                task_id='stage_tables', 
                bash_command="export PYTHONPATH=$AIRFLOW_HOME/dags:$PYTHONPATH; python3 $AIRFLOW_HOME/dags/aplazame_etls/json_to_stage.py")

        dw_tables = BashOperator(
                task_id='dw_tables', 
                bash_command="export PYTHONPATH=$AIRFLOW_HOME/dags:$PYTHONPATH; python3 $AIRFLOW_HOME/dags/aplazame_etls/stage_to_dw.py")

        summary_tables = BashOperator(
                task_id='summary_tables',
                bash_command=spark_submit)

        end = DummyOperator(task_id="end")

# Pipeline
create_schema >> stage_tables >> [dw_tables, summary_tables] >> end

