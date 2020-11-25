from src.drink import Drink
from src.customer import Customer

class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        
        beer = Drink("Beer", 3.00, 2)
        wine = Drink("Wine", 8.00, 6)
        whiskey = Drink("Whiskey", 4.50, 40)
        vodka = Drink("Vodka", 1.00, 30)

        self.drinks = [beer, wine, whiskey, vodka]

    def get_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def increase_customer_drunkeness(self, drink_name, customer):
        drink = self.get_drink_by_name(drink_name)
        customer.drunkeness += drink.alcohol_level


    def sell_drink_to_customer(self, drink_name, customer):
        if customer.age >= 18:
            drink = self.get_drink_by_name(drink_name)
            customer.remove_money_from_wallet(drink.price)
            self.till += drink.price

    




    