import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Simon", 50.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)
        
    def test_pub_has_drinks(self):
        self.assertEqual(4, len(self.pub.drinks))

    def test_get_drink_by_name(self):
        self.assertEqual(self.pub.drinks[0], self.pub.get_drink_by_name("Beer"))

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer("Beer", self.customer)


    
