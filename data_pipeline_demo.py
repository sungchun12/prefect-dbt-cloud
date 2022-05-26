from prefect import flow, task, get_run_logger

@task(name="Extract")
def extract(logger):
    logger.info("Extract Raw Data")

@task(name="Load")
def load(logger):
    logger.info("Load Raw Data")

@task(name="Transform")
def transform(logger):
    logger.info("Transform Raw Data")

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
