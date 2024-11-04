from .product import Product
from .drink import Drink
from .pizza import Pizza


class ProductFactory:
    def create(self, a_dict: dict) -> Product:
        match a_dict:
            case {"nom": name, "volume": volume, "prix": prix}:
                return Drink(name, prix, volume)
            case {"nom": name, "taille": taille, "garnitures": items}:
                pizza = Pizza(name, taille)
                for item in items:
                    pizza.add_ingredient(item)
                return pizza
