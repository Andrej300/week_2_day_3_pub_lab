from src.drink import Drink


class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age 
        self.drunkeness = 0

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def increase_customer_drunkeness(self, alcohol_level):
        self.drunkeness += alcohol_level
    
