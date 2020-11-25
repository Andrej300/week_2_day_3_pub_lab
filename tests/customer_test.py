import unittest 
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Simon", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Simon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink("beer")
        self.assertEqual(47, self.customer.wallet)