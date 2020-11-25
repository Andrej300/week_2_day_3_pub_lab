import unittest 
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Simon", 50.00, 30)

    def test_customer_has_name(self):
        self.assertEqual("Simon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(30, self.customer.age)

    def test_customer_remove_money(self):
        self.customer.remove_money_from_wallet(30)
        self.assertEqual(20, self.customer.wallet)

        