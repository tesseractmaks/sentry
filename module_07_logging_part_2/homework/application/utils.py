
import logging.config

from logging_config import dict_config


logging.config.dictConfig(dict_config)
from typing import Union, Callable
from operator import sub, mul, floordiv, add


logger = logging.getLogger(__name__)
logger_info = logging.getLogger("module_logger_info")
logger_error = logging.getLogger("module_logger_error")
logger_info.setLevel("INFO")
logger_error.setLevel("ERROR")


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger_info.info(f"start - {__name__}")
    if not isinstance(value, str):
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator value")
    logger_info.info(f"finish - {__name__}")
    return OPERATORS[value]
