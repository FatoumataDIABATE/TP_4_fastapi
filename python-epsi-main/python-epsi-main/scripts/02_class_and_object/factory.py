import json


class Animal:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"I'm a {type(self)} and my name is {self.name}"


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Factory:
    def create_dog(self, name: str):
        return Dog(name)

    def create_cat(self, name: str):
        return Cat(name)

    def create(self, item: dict):
        match item:
            case {"type": "cat", "name": name}:
                return self.create_cat(name)
            case {"type": "dog", "name": name}:
                return self.create_dog(name)
            case _:
                raise RuntimeError("Invalid item", item)

    def create_from_dict(self, from_json: list[dict]):
        return [self.create(item) for item in from_json]


if __name__ == '__main__':
    factory = Factory()
    print(factory.create_from_dict([{
        "type": "cat", "name": "Felix"
    }, {
        "type": "dog", "name": "Rocky"
    }]))
