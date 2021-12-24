import unittest
from pizza import Pizza


class TestPizza(unittest.TestCase):
    def test_instance(self):
        pizza = Pizza('pepperoni', 'L')
        self.assertIsInstance(pizza.dict(), dict)

    def test_exception1(self):
        with self.assertRaises(Exception):
            Pizza('pepperon', 'L')

    def test_exception2(self):
        with self.assertRaises(Exception):
            Pizza('pepperoni', 'S')

    def test_equal(self):
        actual = Pizza('pepperoni', 'L')
        expected = Pizza('pepperoni', 'L')
        self.assertEqual(expected, actual)

    def test_bigger(self):
        actual = Pizza('pepperoni', 'L')
        expected = Pizza('pepperoni', 'XL')
        self.assertNotEqual(expected, actual)

    def test_other_type(self):
        actual = Pizza('pepperoni', 'L')
        expected = Pizza('margherita', 'L')
        self.assertNotEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
