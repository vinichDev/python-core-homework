import time
from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        def wrapped(*args, **kwargs):
            sum_func_execution_time = 0
            for i in range(num):
                func_start_time = time.time()
                func(*args, **kwargs)
                func_end_time = time.time()
                func_execution_time = func_end_time - func_start_time
                sum_func_execution_time += func_execution_time
                print(func_execution_time)
            print(sum_func_execution_time / num)
        return wrapped
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
