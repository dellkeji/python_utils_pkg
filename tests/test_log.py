import os

from utils import logger


def test_create_log():
    _log = logger.get_logger(log_file="./test.log", name="test")
    _log.info("this is a test")
    
    assert os.path.exists("./test.log")

    os.remove("./test.log")
