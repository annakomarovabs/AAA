import unittest
from pizza import Pizza


class TestPizza(unittest.TestCase):
    def test_instance(self):
        pizza = Pizza('pepperoni')
        self.assertIsInstance(pizza.dict(), dict)

    def test_exception(self):
        with self.assertRaises(Exception):
            Pizza('pepperon')


if __name__ == '__main__':
    unittest.main()