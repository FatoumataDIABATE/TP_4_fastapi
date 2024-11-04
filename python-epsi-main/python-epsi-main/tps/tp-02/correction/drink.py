from .product import Product

class Drink(Product):
    def __init__(self, name: str, price: float, volume: int):
        super().__init__(name, price)
