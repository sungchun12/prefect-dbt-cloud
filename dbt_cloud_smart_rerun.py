import os
from dataclasses import dataclass

from prefect import flow, task
from prefect_dbt.cloud import DbtCloudCredentials
from prefect_dbt.cloud.runs import get_dbt_cloud_run_artifact
from run_results_parser import dbt_command_run_results_parser

@dataclass(frozen=True)  # make attributes immutable
class dbt_cloud_job_rerun_vars:
    """Basic dbt Cloud job rerun configurations."""

    # add type hints
    run_id: int = os.getenv('RUN_ID')  # 46948860
    status_set: set = os.getenv('STATUS_SET') # {'error','fail','warn'}
    dbt_command_override: str = os.getenv('DBT_COMMAND_OVERRIDE') # "dbt build"
    run_downstream_nodes: bool = bool(os.getenv('RUN_DOWNSTREAM_NODES'))  # True


@task
def parse_run_results_to_dbt_command(artifact, dbt_command_generator):
    dbt_command_output = dbt_command_generator.get_dbt_command_output(run_results=artifact)
    return dbt_command_output

@flow
def smart_rerun_flow():
    dbt_command_generator = dbt_command_run_results_parser(
        dbt_cloud_job_rerun_vars.status_set,
        dbt_cloud_job_rerun_vars.dbt_command_override,
        dbt_cloud_job_rerun_vars.run_downstream_nodes,
    )
    credentials = DbtCloudCredentials(api_key=os.getenv('DBT_TOKEN'), account_id=16173)
    artifact = get_dbt_cloud_run_artifact(
        dbt_cloud_credentials=credentials,
        run_id=dbt_cloud_job_rerun_vars.run_id,
        path="run_results.json"
    )
    dbt_command_output = parse_run_results_to_dbt_command(artifact, dbt_command_generator)
    print(dbt_command_output.result())

smart_rerun_flow()