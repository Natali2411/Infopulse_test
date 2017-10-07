import unittest
from distance import distance

class TestDistance(unittest.TestCase):
    def test_zero(self):
        res = distance(0,0,0,0)
        self.assertEqual(res, 0)

    def test_negative(self):
        res = distance(-1,-5,-6,-4)
        self.assertEqual(res, -10)

    def test_type(self):
        res = distance(5,6,7,'fjhd')
        self.assertEqual(res, 'fdfhdshf')