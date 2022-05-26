from prefect import flow, task, get_run_logger

# from prefect.tasks.dbt import DbtCloudRunJob # this does NOT work because this library doesn't exist in Orion yet
# import os
# from dotenv import load_dotenv

# load the .env file
# load_dotenv()

# TODO: add a dbt Cloud job example
# dbt_cloud = DbtCloudRunJob(cause="prefect-flow", wait_for_job_run_completion=True)


@task(name="Extract")
def extract(logger):
    logger.info("Extract Raw Data")


@task(name="Load")
def load(logger):
    logger.info("Load Raw Data")


@task(name="Transform")
def transform(logger):
    logger.info("Transform Raw Data")
    # TODO: add a dbt Cloud job example
    # account_id = os.getenv["ACCOUNT_ID"]
    # job_id = os.getenv["JOB_ID"]
    # token = os.getenv["TOKEN"]
    # dbt_job = dbt_cloud(
    #     account_id=account_id, job_id=job_id, token=token
    # )
    # dbt_job.run()


@task(name="Predict")
def predict(logger):
    logger.info("Predict results on transformed data")


@flow(name="Full Data Pipeline")
def data_pipeline():
    logger = get_run_logger()
    extract(logger)
    load(logger)
    transform(logger)
    predict(logger)


if __name__ == "__main__":
    data_pipeline()
