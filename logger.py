import logging


def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger("devops-core-tooling")


def get_logger_name():
    return "devops-core-tooling"
