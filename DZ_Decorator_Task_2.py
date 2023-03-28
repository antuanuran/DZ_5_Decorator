import os
import datetime
from time import sleep


def logger(path=None):

    def _logger(old_function):

        def wrapper(*args, **kwargs):
            time_start = datetime.datetime.now()
            result = old_function(*args, **kwargs)

            print(f'Функция "{old_function.__name__}" запущена...')
            sleep(0.3)
            print(f'Данные сохранены в файл: {path}\n')
            sleep(0.7)

            with open(path, 'a') as fd:
                fd.write(f'{time_start} | {old_function.__name__} | {args=} | {kwargs=} | {result=}\n')
            return result

        return wrapper

    return _logger


# Результат.
def test_1():
    # logger_decorator = logger(path='log_hello.txt')

    # @logger_decorator
    # def hello_world():
    #     return 'Hello World'

    @logger(path='log_hello.txt')
    def hello_world():
        return 'Hello World'

    @logger(path='log_summator.txt')
    def summator(a, b=0):
        return a + b

    @logger(path='log_div.txt')
    def div(a, b):
        return a / b

    hello_world()
    summator(2, 2)
    div(6, 2)
    summator(4.3, b=2.2)
    summator(a=0, b=0)


if __name__ == '__main__':
    test_1()
