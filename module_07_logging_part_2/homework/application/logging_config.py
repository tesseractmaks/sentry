import logging
import sys
import string


class ContextFilter(logging.Filter):

    def filter(self, record):
        for char in record.msg:
            if char not in string.printable:
                break
        else:
            return True


# class LoggHandler(logging.Handler):
#     def __init__(self, file_name, mode="a"):
#         super().__init__()
#         self.file_name = file_name
#         self.mode = mode
#
#     def emit(self, record):
#         message = self.format(record)
#         with open(self.file_name, mode=self.mode) as file:
#             file.write(message + "\n")



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
            "level": "INFO",
            "formatter": "base",
            "stream": sys.stderr,
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "h",
            "interval": 10,
            "backupCount": 5,
            "level": "INFO",
            "formatter": "base",
            "filename": "logfile_info.log",
            # "mode": "a"
        },
        "file_err": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "h",
            "interval": 10,
            "backupCount": 5,
            "level": "ERROR",
            "formatter": "base",
            "filename": "logfile_error.log",
            # "mode": "a"
        }
    },
    "loggers": {
        "module_logger_info": {
            "level": "INFO",
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