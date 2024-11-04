import functools
import time
from collections.abc import Callable

def timer(func: Callable[[], None]):
    def wrapper():
        t0 = time.time()
        func()
        print("Function took", time.time() - t0)
    return wrapper


@timer
def aaaa():
    time.sleep(3)

@timer
def bbbb():
    time.sleep(3)

# t0 = time.time()
# print("Function took", time.time() - t0)


# fct = timer(aaaa)
# fct()

def cache(func):
    memory: dict[int, int] = {}

    def wrapper(n: int):
        print("Checking if ", n, "is in memory")
        if n in memory:
            print("Found it")
            return memory[n]
        print("Storing new value")
        memory[n] = func(n)
        return memory[n]
    return wrapper

# @functools.cache
@cache
def fibbonaci(n: int):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibbonaci(n - 1) + fibbonaci(n - 2)

print(fibbonaci(100))

