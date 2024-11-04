import json

from correction.factory import ProductFactory
from correction.order import Order
from correction.product import Product

menu: dict[str, Product] = dict()

factory = ProductFactory()

with open("menu.json", "r") as fp:
    menu_as_json = json.load(fp)

for drink in menu_as_json["boissons"]:
    product: Product = factory.create(drink)
    menu[product.name()] = product

for pizza in menu_as_json["pizzas"]:
    product = factory.create(pizza)
    menu[product.name()] = product

with open("commandes.json") as fp:
    for command in json.load(fp):
        order = Order(command["commande_id"])
        for item in command["items"]:
            order.add(menu[item])

        print(order)


