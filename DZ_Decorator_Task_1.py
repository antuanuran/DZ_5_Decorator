import os
import datetime
from time import sleep


def logger(old_function):

    def wrapper(*args, **kwargs):
        time_start = datetime.datetime.now()
        result = old_function(*args, **kwargs)

        print(f'Функция "{old_function.__name__}" запущена...')
        sleep(1)

        with open('main.log', 'a') as fd:
            fd.write(f'{time_start} | {old_function.__name__} | {args=} | {kwargs=} | {result=}\n')
        return result
    # wrapper.__name__ = old_function.__name__      # На случай, если нужно получать реальные названия функций вместо оберток

    return wrapper


# Результат.
def test_1():

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    hello_world()
    summator(2, 2)
    div(6, 2)
    summator(4.3, b=2.2)
    summator(a=0, b=0)


if __name__ == '__main__':
    test_1()




































# ***************************************
# def logger(old_function):
#
#     def new_func(*args, **kwargs):
#         print('Запускаем обёртку')
#         return old_function(*args, **kwargs)
#
#     return new_func
#
#
# def summ(a, b):
#     c = a + b
#     print(c)
#     return c
#
#
# summ = logger(summ)
# summ(2, 3)
# *******************************************
















