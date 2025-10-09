""" 迭代器中可以有入参 """

import time

def timeit(inte: int) -> callable:

    def inner(func):

        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(inte):
                res = func(*args, **kwargs)
            cost = time.time() - start
            print("cost:", cost)
            return res
        return wrapper
    return inner

@timeit(10000000)   # 大约0.5秒迭代10000000次
def double(x):
    return x * 2

double(2)