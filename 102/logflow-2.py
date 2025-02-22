from prefect import flow, get_run_logger


@flow(name="log-example-flow")
def log_it():
    logger = get_run_logger()
    logger.info("INFO level log message.")


if __name__ == "__main__":
    log_it()
