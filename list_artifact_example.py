import os
from prefect import flow

from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.jobs import list_dbt_cloud_run_artifacts

@flow
def list_artifacts_flow():
    credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)

    artifact_list = list_dbt_cloud_run_artifacts(
        dbt_cloud_credentials=credentials,
        run_id=66585620
    )
    print(artifact_list.result())

list_artifacts_flow()