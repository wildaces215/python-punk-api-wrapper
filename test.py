import unittest
from beer import *

"""
Tests for Python wrapper
"""


class statusCodes(unittest.TestCase):

    def testOne(self):
        self.assertEqual(get_404(), 404)

    def testtwo(self):
        self.assertEqual(len(beer_name_data('landshark')), 2)

    def testThree(self):
        self.assertEqual(random_beer(), )


if __name__ == '__main__':
    unittest.main()
