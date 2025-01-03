"""
logger module

custom logger class for logging
"""
import logging
import sys
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

DEFAULT_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

class CustomLogger(Logger):
    def __init__(self, log_file=None, log_format=DEFAULT_FORMAT, *args, **kwargs):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file

        Logger.__init__(self, *args, **kwargs)

        self.addHandler(self.get_console_handler())
        if log_file:
            self.addHandler(self.get_file_handler())

        # with this pattern, it's rarely necessary to propagate the| error up to parent
        self.propagate = False

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.log_file, when="midnight")
        file_handler.setFormatter(self.formatter)
        return file_handler



def get_logger(log_file=None, log_format=DEFAULT_FORMAT, *args, **kwargs) -> Logger:
    return CustomLogger(log_file=log_file, log_format=log_format, *args, **kwargs)
