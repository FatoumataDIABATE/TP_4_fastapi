import pytest
from pizzeria import Ingredient, Pizza, Drink, Order, ProductFactory

# Étape 1 : Test de la classe Pizza et Drink

def test_ingredient():
    ingredient = Ingredient("Fromage")
    assert ingredient.name == "Fromage"

def test_pizza_creation():
    pizza = Pizza("Margherita", "moyenne", price=10)
    pizza.add_ingredient(Ingredient("Fromage"))
    pizza.add_ingredient(Ingredient("Tomate"))

    assert pizza.nom == "Margherita"
    assert pizza.size == "moyenne"
    assert pizza.price == 10
    assert len(pizza.ingredients) == 2  # Vérifie si deux ingrédients ont été ajoutés

def test_drink_creation():
    drink = Drink("Coca-Cola", 500, 2)

    assert drink.name == "Coca-Cola"
    assert drink.volume == 500
    assert drink.price == 2

# Étape 2 : Test de la classe Order

def test_add_product_to_order():
    pizza = Pizza("Margherita", "moyenne", price=10)
    drink = Drink("Coca-Cola", 500, 2)

    order = Order(1)
    order.add_product(pizza)
    order.add_product(drink)

    assert len(order.products) == 2  # Vérifie que la commande contient bien 2 produits
    assert order.total() == 12  # Vérifie que le total est correct

# Étape 3 : Test de la ProductFactory et du pattern matching

def test_product_factory():
    # Tester la création d'une pizza
    pizza = ProductFactory.create_product("pizza", "Margherita", 10, "Fromage", "Tomate")
    assert isinstance(pizza, Pizza)
    assert pizza.nom == "Margherita"
    assert pizza.price == 10
    assert len(pizza.ingredients) == 2

    # Tester la création d'une boisson
    drink = ProductFactory.create_product("drink", "Coca-Cola", 2, 500)
    assert isinstance(drink, Drink)
    assert drink.name == "Coca-Cola"
    assert drink.price == 2
    assert drink.volume == 500

# Bonus : Test de la fonction de lecture des commandes

def test_command_reading():
    # Test d'une commande générée via le fichier commandes.json
    commands = [
        {"commande_id": 1, "items": [
            "Pesto", "Sprite", "Jus d'orange", "Coca-Cola", "Végétarienne"
        ]}
    ]

    command = Order(1)
    for item in commands[0]['items']:
        product = ProductFactory.create_product("drink", item, 2, 500) if "Coca-Cola" in item else ProductFactory.create_product("pizza", item, 10)
        command.add_product(product)

    assert len(command.products) == 5
    assert command.total() > 0  # Vérifie que la commande a un total correct

