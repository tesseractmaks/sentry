import logging.config

import sys

from logging_config import dict_config, ContextFilter
from utils import string_to_operator

logging.config.dictConfig(dict_config)


def calc(args):
    logger_info.info(f"Arguments: {args}")
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]
    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger_error.error(f"Error while converting number 1 {e}")
    try:
        num_2 = float(num_2)
    except ValueError as e:
       logger_error.error(f"Error while converting number 1 {e}")
    operator_func = string_to_operator(operator)
    result = operator_func(num_1, num_2)
    logger_info.info(f"Result:  {result}")


if __name__ == '__main__':
    logger_info = logging.getLogger("module_logger_info")
    logger_error = logging.getLogger("module_logger_error")
    logger_info.setLevel("INFO")
    logger_error.setLevel("ERROR")
    filt = ContextFilter()
    logger_info.addFilter(filt)
    logger_error.addFilter(filt)
    calc(sys.argv[1:])







