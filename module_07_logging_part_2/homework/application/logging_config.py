import logging
import shlex
import subprocess
import sys
import string


class ContextFilter(logging.Filter):

    def filter(self, record):
        for char in record.msg:
            if char not in string.printable:
                break
        else:
            return True


class CustomFileHandler(logging.Handler):

    def __init__(self, file_name, mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        data = f'{message}'
        server_url = "http://127.0.0.1:5000/logs"
        template = f'curl -H "Content-Type: application/json" -X POST -d \"{data}\" {server_url}'
        curl_cmd = shlex.split(template)
        response = subprocess.Popen(curl_cmd, stdout=subprocess.PIPE, universal_newlines=True)
        response.stdout.read()
        with open(self.file_name, mode=self.mode) as file:
            file.write(message + '\n')


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
            "()": CustomFileHandler,
            "level": "INFO",
            "formatter": "base",
            "file_name": "logfile.log",
            "mode": "a"
        },
        "file_err": {
            "()": CustomFileHandler,
            "level": "ERROR",
            "formatter": "base",
            "file_name": "logfile_error.log",
            "mode": "a"
        },
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



