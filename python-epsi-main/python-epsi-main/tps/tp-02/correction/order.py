from .product import Product


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []

    def add(self, item: Product):
        self.items.append(item)

    def total(self) -> int:
        return sum(map(Product.price, self.items))