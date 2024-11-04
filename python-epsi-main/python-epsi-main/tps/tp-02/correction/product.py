class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def price(self):
        return self._price

    def name(self):
        return self._name