import logging.config
import sys

from mod_logger import dict_config
from utils import string_to_operator


def calc(args):
    logger_debug.debug(f"Arguments: {args}")
    print("Arguments: ", args)

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
    logger_debug.debug(f"Result:  {result}")
    print("Result: ", result)
    print(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    logging.config.dictConfig(dict_config)

    logger_debug = logging.getLogger("module_logger_debug")
    logger_error = logging.getLogger("module_logger_error")
    logger_debug.setLevel("DEBUG")
    logger_error.setLevel("ERROR")



    # logging.basicConfig(
    #     level=logging.DEBUG, filename='logs.log',
    #     format='%(levelname)s --- %(name)s - %(asctime)s %(message)s',
    #     filemode="w"
    # )
    calc(sys.argv[1:])
