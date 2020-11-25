from src.drink import Drink

class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        beer = Drink("Beer", 3.00)
        wine = Drink("Wine", 8.00)
        whiskey = Drink("Whiskey", 4.50)
        vodka = Drink("Vodka", 1.00)
        self.drinks = [beer, wine, whiskey, vodka]

    