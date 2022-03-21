import base64

command = b"aW1wb3J0IGxvZ2dpbmcKaW1wb3J0IG9zCmltcG9ydCBzdHJpbmcKCmxvZ2dlciA9IGxvZ2dpbmcu\nZ2V0TG9nZ2VyKF9fbmFtZV9fKQoKCmRlZiBmdW5jMSgpOgogICAgbG9nZ2VyLmluZm8oItCo0LDQ\nsyAxIikKICAgIGxvZ2dlci5kZWJ1Zygi0K3RgtC+INC/0YDQvtGB0YLQviDRgNCw0LfQvNC40L3Q\nutCwIikKCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGRhdGEgPSBpbnB1dCgi0JLQsNGIINC+0YLQ\nstC10YI/ICIpCgogICAgICAgIHRyeToKICAgICAgICAgICAgbnVtYmVyID0gaW50KGRhdGEpCgog\nICAgICAgICAgICBpZiBudW1iZXIgIT0gOTk3MzoKICAgICAgICAgICAgICAgIGxvZ2dlci5kZWJ1\nZygi0J3QsNC8INC90YPQttC90L4g0LzQsNC60YHQuNC80LDQu9GM0L3QvtC1INC/0YDQvtGB0YLQ\nvtC1INGH0LjRgdC70L4g0LzQtdC90YzRiNC10LUg0YfQtdC8IDEwMDAwIikKICAgICAgICAgICAg\nICAgIHByaW50KCLQndC1INC/0YDQsNCy0LjQu9GM0L3QviEiKQogICAgICAgICAgICBicmVhawog\nICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKCiAgICBwcmludCgi0KjQ\nsNCzIDEg0L/RgNC+0LnQtNC10L0iKQoKCmRlZiBmdW5jMigpOgogICAgbG9nZ2VyLmluZm8oItCo\n0LDQsyAyIikKCiAgICBsb2dnZXIuZGVidWcoItCX0LDQtNCw0LnRgtC1INC/0LXRgNC10LzQtdC9\n0L3QvtC5INC+0LrRgNGD0LbQtdC90LjRjyBTS0lMTEJPWCDQt9C90LDRh9C10L3QuNC1IGF3ZXNv\nbWUiKQogICAgbG9nZ2VyLmRlYnVnKCLQktGLINC80L7QttC10YLQtSDQt9Cw0LTQsNGC0Ywg0LfQ\nvdCw0YfQtdC90LjQtSDQv9C10YDQtdC80LXQvdC90L7QuSDQvtC60YDRg9C20LXQvdC40Y8g0LLQ\nvtGCINGC0LDQujoiKQogICAgbG9nZ2VyLmRlYnVnKCIkIGV4cG9ydCBWQVJOQU1FPXZhbHVlIikK\nCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGlucHV0KCLQlNC70Y8g0L/RgNC+0LTQvtC70LbQtdC9\n0LjRjyDQvdCw0LbQvNC40YLQtSBFTlRFUi4uLiIpCgogICAgICAgIHRyeToKICAgICAgICAgICAg\naWYgb3MuZW52aXJvblsiU0tJTExCT1giXS5sb3dlcigpID09ICJhd2Vzb21lIjoKICAgICAgICAg\nICAgICAgIGJyZWFrCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwoK\nICAgICAgICBwcmludCgi0JLRiyDQvdC1INCz0L7RgtC+0LLRiy4uLiIpCgogICAgcHJpbnQoItCo\n0LDQsyAyINC/0YDQvtC50LTQtdC9IikKCgpkZWYgZnVuYzMoKToKICAgIGxvZ2dlci5pbmZvKCLQ\nqNCw0LMgMyIpCgogICAgbG9nZ2VyLmRlYnVnKCLQodC+0LfQtNCw0LnRgtC1INGE0LDQudC7IGh3\nNy50eHQg0YEg0LDQvdCz0LvQuNC50YHQutC40Lwg0L/QsNC70LjQvdC00YDQvtC80L7QvCDQstC9\n0YPRgtGA0LgiKQogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGlucHV0\nKCLQlNC70Y8g0L/RgNC+0LTQvtC70LbQtdC90LjRjyDQvdCw0LbQvNC40YLQtSBFTlRFUi4uLiIp\nCgogICAgICAgICAgICB3aXRoIG9wZW4oImh3Ny50eHQiLCAiciIpIGFzIGZpOgogICAgICAgICAg\nICAgICAgZGF0YSA9IGZpLnJlYWQoKS5sb3dlcigpCgogICAgICAgICAgICAgICAgZGF0YV9zdHIg\nPSBbaXQgZm9yIGl0IGluIGRhdGEgaWYgaXQgaW4gc3RyaW5nLmFzY2lpX2xvd2VyY2FzZV0KCiAg\nICAgICAgICAgICAgICBpZiBkYXRhX3N0ciA9PSBkYXRhX3N0cls6Oi0xXToKICAgICAgICAgICAg\nICAgICAgICBicmVhawoKICAgICAgICAgICAgICAgIGxvZ2dlci5kZWJ1ZyhmIntkYXRhX3N0cn0g\nIT0ge2RhdGFfc3RyWzo6LTFdfSIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAg\nICAgcGFzcwoKICAgICAgICBwcmludCgi0J3QtSDRgNCw0LHQvtGC0LDQtdGCLi4uIikKCiAgICBw\ncmludCgi0KjQsNCzIDMg0L/RgNC+0LnQtNC10L0iKQoKCmRlZiB3aGF0X3dlbnRfd3JvbmcoKToK\nICAgIGZ1bmMxKCkKICAgIGZ1bmMyKCkKICAgIGZ1bmMzKCkKCgp3aGF0X3dlbnRfd3JvbmcoKQo="

if __name__ == "__main__":
    exec(base64.decodebytes(command).decode("utf8"))

message_bytes = base64.b64decode(command)
message = message_bytes.decode('utf-8')
# print(message)
# TODO В строке выше закодирован этот код:

import logging
import os
import string

logger = logging.getLogger(__name__)


def func1():
    logger.info("Шаг 1")
    logger.debug("Это просто разминка")

    while True:
        data = input("Ваш ответ? ")

        try:
            number = int(data)

            if number != 9973:
                logger.debug("Нам нужно максимальное простое число меньшее чем 10000")
                print("Не правильно!")
            break
        except Exception:
            pass

    print("Шаг 1 пройден")


def func2():
    logger.info("Шаг 2")

    logger.debug("Задайте переменной окружения SKILLBOX значение awesome")
    logger.debug("Вы можете задать значение переменной окружения вот так:")
    logger.debug("$ export VARNAME=value")

    while True:
        input("Для продолжения нажмите ENTER...")

        try:
            if os.environ["SKILLBOX"].lower() == "awesome":
                break
        except Exception:
            pass

        print("Вы не готовы...")

    print("Шаг 2 пройден")


def func3():
    logger.info("Шаг 3")

    logger.debug("Создайте файл hw7.txt с английским палиндромом внутри")
    while True:
        try:
            input("Для продолжения нажмите ENTER...")

            with open("hw7.txt", "r") as fi:
                data = fi.read().lower()

                data_str = [it for it in data if it in string.ascii_lowercase]

                if data_str == data_str[::-1]:
                    break

                logger.debug(f"{data_str} != {data_str[::-1]}")
        except Exception:
            pass

        print("Не работает...")

    print("Шаг 3 пройден")


def what_went_wrong():
    func1()
    func2()
    func3()


what_went_wrong()
