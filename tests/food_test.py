import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Pizza", 5, 10)

    def test_food_has_name(self):
        self.assertEqual("Pizza", self.food.name)

    
    def test_food_has_price(self):
        self.assertEqual(5, self.food.price)

    def test_rejuvenation_level(self):
        self.assertEqual(10, self.food.rejuvenation_level)
