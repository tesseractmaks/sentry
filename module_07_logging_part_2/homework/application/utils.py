import logging

from typing import Union, Callable
from operator import sub, mul, floordiv, add


logger = logging.getLogger(__name__)


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
    if not isinstance(value, str):
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
