import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_neg_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-2), "error age input")

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(35), 150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(63), 100)

if __name__ == '__main__':
    unittest.main()