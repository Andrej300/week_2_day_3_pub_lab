from src.drink import Drink
from src.food import Food
from src.customer import Customer

class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        
        beer = Drink("Beer", 3.00, 2)
        wine = Drink("Wine", 8.00, 6)
        whiskey = Drink("Whiskey", 4.50, 40)
        vodka = Drink("Vodka", 1.00, 30)

        pizza = Food("Pizza", 5, 10)
        burger = Food("Burger", 4.50, 8)

        self.food = [pizza, burger]
        self.drinks = [beer, wine, whiskey, vodka]

    def get_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
    
    def get_food_by_name(self, food_name):
        for item in self.food:
            if item.name == food_name:
                return item
    
    def add_money_to_till(self, amount):
        self.till += amount

    def sell_drink_to_customer(self, drink_name, customer):
        if customer.age >= 18 and customer.drunkeness < 50:
            drink = self.get_drink_by_name(drink_name)
            customer.remove_money_from_wallet(drink.price)
            self.add_money_to_till(drink.price)
            customer.increase_customer_drunkeness(drink.alcohol_level)
    

    def sell_food_to_customer(self, food_name, customer):
        food = self.get_food_by_name(food_name)
        customer.remove_money_from_wallet(food.price)
        self.add_money_to_till(food.price)
        customer.decrease_drunkeness(food.rejuvenation_level)

        




    