import os

from prefect import flow, task
from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.runs import get_dbt_cloud_run_artifact

@flow
def get_artifact_task():
    credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)
    artifact = get_dbt_cloud_run_artifact(
        dbt_cloud_credentials=credentials,
        run_id=66585620,
        path="run_results.json"
    )

    return artifact
  
@flow
def parse_artifact_task(artifact):
    artifact_result = artifact.result()
    print(artifact_result)
    return artifact_result

@flow
def smart_rerun_flow():
    artifact = get_artifact_task()
    parse_artifact_task(artifact)

smart_rerun_flow()