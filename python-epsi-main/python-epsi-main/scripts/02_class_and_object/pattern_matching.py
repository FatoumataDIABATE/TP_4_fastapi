import functools
import time
from random import random, randint
from unittest import addModuleCleanup

class Timer:
    def __init__(self, description: str):
        self.description = description

    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Duration:", time.time() - self.t0)


i = 10
#
@functools.lru_cache(maxsize=500)
def fibonaci(n: int):
    print("Was called with", n)
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibonaci(n - 2) + fibonaci(n - 1)

with Timer("Fib"):
    fibonaci(500)




#
# point = 0
#
# def describe_point(point):
#     a,b = point
#
#     match point:
#         case (0, 0):
#             return "Origine"
#         case (0, y):
#             return f"Axe Y, à {y}"
#         case (x, 0):
#             return f"Axe X, à {x}"
#         case (x, y):
#             return f"Point à ({x}, {y})"
#         case _:
#             return "C'est autre chose"
#
# class Animal:
#     def __init__(self, name: str, age: int):
#         self.age = age
#         self.name = name
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# animals = [Dog("Rocky", 10), Cat("Felix", 3)]
#
# def process(animal: Animal):
#     # if isinstance(animal, Dog):
#     #     print("C'est un chien")
#     match animal:
#         case Dog(name="Rocky", age=age) as rocky:
#             print("C'est Rocky, il a ", age)
#         case Dog() as dog:
#             pass
#         case Cat() as cat:
#             pass
#
# class Timer:
#     def __init__(self, description: str):
#         self.description = description
#
#     def __enter__(self):
#         self.t0 = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Duration:", time.time() - self.t0)
#
# #
# # timer = Timer("Exemple")
# # with timer:
# #     time.sleep(3)
#
# # def is_prime(n: int):
# #     pass
#
# # with open("something.txt", "r") as fp:
# #     for line in fp:
# #         print(line)
#
#
#
# def generator():
#     print("Create generator")
#     i = 0
#     while True:
#         yield randint(0, 1_000_000)
#         i += 1
#         #
#         # if i == 1000:
#         #     break
# #
# # for nb in generator():
# #     print(nb)
#
# g = generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))