import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Simon", 50.00, 30)
        self.underage_customer = Customer("Andre", 30.00, 15)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)
        
    def test_pub_has_drinks(self):
        self.assertEqual(4, len(self.pub.drinks))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(20)
        self.assertEqual(120, self.pub.till)

    def test_get_drink_by_name(self):
        self.assertEqual(self.pub.drinks[0], self.pub.get_drink_by_name("Beer"))

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer("Beer", self.customer)
        self.assertEqual(47, self.customer.wallet)
        self.assertEqual(103, self.pub.till)

    def test_sell_drink_to_underage_customer(self):
        self.pub.sell_drink_to_customer("Beer", self.underage_customer)
        self.assertEqual(30, self.underage_customer.wallet)
        self.assertEqual(100, self.pub.till)

    def test_increase_customer_drunkeness(self):
        self.pub.increase_customer_drunkeness("Vodka", self.customer)
        self.assertEqual(30, self.customer.drunkeness)

    def test_customer_increases_drunkeness(self):
        self.pub.sell_drink_to_customer("Whiskey", self.customer)
        self.assertEqual(40, self.customer.drunkeness)

    def test_resfuse_sale(self):
        self.pub.sell_drink_to_customer("Whiskey", self.customer)
        self.pub.sell_drink_to_customer("Whiskey", self.customer)
        self.pub.sell_drink_to_customer("Vodka", self.customer)
        self.assertEqual(80, self.customer.drunkeness)

    

    

    





    
