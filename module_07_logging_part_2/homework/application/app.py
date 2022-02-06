import logging.config
import shlex, subprocess
import sys

from logging_config import dict_config, ContextFilter
from utils import string_to_operator

logging.config.dictConfig(dict_config)
# TODO запуск приложения файл -  app_logger.py

# TODO когда подрубаю fileConfig, то выходит ошибка 'KeyError: 'qualname'' этот параметр есть глубоко внутрии
#  библиотеки и я не могу понять как на нашем уровне исправить. У нас здесь нигде нет ничего похожего на 'qualname'
# logging.config.fileConfig('logging_conf.ini', disable_existing_loggers=False)


def calc(args):
    # TODO здесь просто передаю объект логгера в переменную 'code', но это не правильно, данных нет
    code = logger_info.info(f"Arguments: {args}")

    print("Arguments: ", args)
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        code = logger_error.error(f"Error while converting number 1 {e}")

    try:
        num_2 = float(num_2)
    except ValueError as e:
        code = logger_error.error(f"Error while converting number 1 {e}")

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)
    # code = logger_info.info(f"Result:  {result}")
    print("Result: ", result)
    print(f"{num_1} {operator} {num_2} = {result}")
    # TODO здесь передаю объект логгера {code} в  параметр запроса
    command_str = f'curl -X POST http://127.0.0.1:5000/logs --data {code}'
    command = shlex.split(command_str)
    # TODO здесь код перестает работать переменная "result" не получает данные,
    #  даже если прописать тестовую строку в {code}
    #  В Postman все работает!
    result = subprocess.run(command, capture_output=True)
    decode_result = result.stdout.decode('utf-8')
    print(decode_result)
    return decode_result

# TODO вопрос: не пойму как передать каждый логер в строку curl.
#  Не передавать же в каждом случае всю строку в пвраметр curl так:
#  command_str = f'curl -X POST http://127.0.0.1:5000/logs --data {logger_error.error(f"Error while converting number 1 {e}")}'


if __name__ == '__main__':

    logger_info = logging.getLogger("module_logger_info")
    logger_error = logging.getLogger("module_logger_error")
    logger_info.setLevel("INFO")
    logger_error.setLevel("ERROR")
    filt = ContextFilter()
    logger_info.addFilter(filt)
    logger_error.addFilter(filt)
    # TODO думаю что где-то здесь нужно ловить логгеры для curl так:
    #  command_str = f'curl -X POST http://127.0.0.1:5000/logs --data {logger_info....}'
    #  но никак не могу найти параметр  у logger_info. для распечатывания

    # calc(sys.argv[1:])





