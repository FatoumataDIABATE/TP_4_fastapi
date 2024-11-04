from multiprocessing.managers import Value


class Player:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise ValueError("Name must be defined")
        self.__name = name


greg = Player("Greg")
greg.name = ""

print("Player name is ", greg.name)

