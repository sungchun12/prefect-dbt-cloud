import os

from prefect import flow
from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.runs import get_dbt_cloud_run_artifact

@flow
def get_artifact_flow():
    credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)
    artifact = get_dbt_cloud_run_artifact(
        dbt_cloud_credentials=credentials,
        run_id=66585620,
        path="run_results.json"
    )
    print(artifact.result())
    return artifact

get_artifact_flow()