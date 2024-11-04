from .product import Product

class Pizza(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        self.items = []

    def add_ingredient(self, ingredient: str):
        self.items.append(ingredient)