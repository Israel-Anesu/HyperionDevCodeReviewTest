import unittest

from hamming import *

#TestingClass
class TestClass(unittest.TestCase):

    def test_calc_redundant_bits(self):
        self.assertEqual(type(int))

    def test_pos_redundant_bits(self):
        self.assertListEqual(type(list))

    def test_alc_parity_bits(self):
        self.assertListEqual()

    def test_detect_error(self):
        self.assertEqual(type(int))

if __name__ == '__main__':
    unittest.main()