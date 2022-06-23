import asyncio
import os

from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.jobs import trigger_dbt_cloud_job_run_and_wait_for_completion

asyncio.run(
    trigger_dbt_cloud_job_run_and_wait_for_completion(
        dbt_cloud_credentials=DbtCloudCredentials(
            api_key=os.getenv('DBT_TOKEN'), account_id=16173
        ),
        job_id=30605,
    )
)
