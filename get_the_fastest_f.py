import time
from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
f = [factorial_classic, factorial_recurrent, factorial]
def get_the_fastest_func(funcs, arg):
    times={}

    for i in funcs:
        start_time = time.monotonic()
        i(arg)
        end_time = time.monotonic()
        times[end_time-start_time]=i
    return times[min(times)]



print(get_the_fastest_func(f, 900))