import os

from prefect import flow, task
from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.runs import get_dbt_cloud_run_artifact

# @task
# def get_artifact_task():
#     credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)
#     artifact = get_dbt_cloud_run_artifact(
#         dbt_cloud_credentials=credentials,
#         run_id=66585620,
#         path="run_results.json"
#     )

#     return artifact
  
@task
def parse_artifact_task(artifact):
    print(artifact)

@flow
def smart_rerun_flow():
    credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)
    artifact = get_dbt_cloud_run_artifact(
        dbt_cloud_credentials=credentials,
        run_id=66585620,
        path="run_results.json"
    )
    parse_artifact_task(artifact)

smart_rerun_flow()