
import logging


class LoggHandler(logging.Handler):
    def __init__(self, file_name, mode="a"):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record):
        message = self.format(record)
        with open(self.file_name, mode=self.mode) as file:
            file.write(message + "\n")


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "()": LoggHandler,
            "level": "DEBUG",
            "formatter": "base",
            "file_name": "logfile_debug.log",
            "mode": "a"
        },
        "file_err": {
            "()": LoggHandler,
            "level": "ERROR",
            "formatter": "base",
            "file_name": "logfile_error.log",
            "mode": "a"
        }
    },
    "loggers": {
        "module_logger_debug": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False,
        },
        "module_logger_error": {
            "level": "ERROR",
            "handlers": ["file_err", "console"],
            # "propagate": False,
        }
    },
}