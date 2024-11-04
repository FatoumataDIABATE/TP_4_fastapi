import abc
import enum
import time
from typing import Self


class AngryException(RuntimeError):
    pass


class IAmAKittenException(RuntimeError):
    pass


class Gender(enum.IntEnum):
    MALE = 1
    FEMALE = 2

    @staticmethod
    def rand():
        return Gender.MALE if time.time() % 2 == 0 else Gender.FEMALE


class Animal(abc.ABC):
    def __init__(self, gender: Gender):
        self.gender = gender

    @abc.abstractmethod
    def __add__(self, other: "Animal") -> Self:
        pass


class Cat(Animal):
    def __init__(self, gender: Gender):
        super().__init__(gender)

    def __add__(self, other: "Animal") -> Self:
        match other:
            case Cat(gender=gender):
                if gender != self.gender:
                    return Kitten(Gender.rand())
                raise AngryException("Cat's don't like other same gender cats")
            case Animal():
                raise AngryException("Cats don't like other animals")


class Kitten(Cat):
    def __add__(self, other: "Animal") -> Self:
        raise IAmAKittenException()


mr = Cat(Gender.MALE)
mr2 = Cat(Gender.MALE)
ms = Cat(Gender.FEMALE)

print(mr + ms)
# try:
print(mr + mr2)
# except AngryException:
#     pass

try:
    undefined = Animal(Gender.MALE)
except TypeError:
    pass
