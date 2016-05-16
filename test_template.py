#!/usr/bin/env
import unittest


class TestNumbers(unittest.TestCase):
    """
    This class was created for my own learning purposes.
    I'm experimenting with the 'unittests' Python module here.
    """
    numberOne = None
    numberTwo = None
    # Number three will be created & instantiated by the setup
    numberTen = None

    def setUp(self):
        """
        Sets up the variables
        :return:
        """
        self.numberOne = 1
        self.numberTwo = 2
        self.numberThree = 3
        self.numberTen = 10

    def test_cumulative(self):
        """
        Tests the correctness of variable instantiation by adding them up.
        :return:
        """
        expected = 10
        # Count up to ten using the declared variables
        actual = self.numberOne + self.numberOne + self.numberTwo + self.numberThree + self.numberThree
        self.assertEqual(actual, expected)

    def test_division(self):
        """
        Tests the correctness of variable instantiation by subtracting with them.
        :return:
        """
        expected = 1
        actual = self.numberTen - self.numberThree - self.numberThree - self.numberOne - self.numberOne

        self.assertEqual(actual, expected)


# This makes sure the module is ran when called directly (e.g. from the commandline)
if __name__ == '__main__':
    unittest.main()
