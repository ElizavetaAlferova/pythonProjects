import time

def add(a, b, c):
    time.sleep(3)
    return a + b + c
def calculate_it(func, *args):
    start_time = time.monotonic()
    a = func(*args)
    end_time = time.monotonic()
    return (a,end_time-start_time)


print(calculate_it(add, 1, 2, 3))