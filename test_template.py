#!/usr/bin/env
import unittest
import mymodule


class TestNumbers(unittest.TestCase):
    """
    This class was created for my own learning purposes.
    I'm experimenting with the 'unittests' Python module here.
    """
    numberOne = None
    numberTwo = None
    # Number three will be created & instantiated by the setup
    numberTen = None
    calc = None

    def setUp(self):
        """
        Sets up the variables
        :return:
        """
        self.numberOne = 1
        self.numberTwo = 2
        self.numberThree = 3
        self.numberTen = 10
        self.calc = mymodule.Calculator()

    def test_cumulative(self):
        """
        Test the add methods of my class 'Calculator' in module 'mymodule.py'.
        Also tests the correctness of variable instantiation by adding them up.
        :return:
        """
        # Test single addition
        expected = 5
        actual = mymodule.Calculator.add(self.numberTwo, self.numberThree)
        self.assertEqual(actual, expected, 'single addition failed')

        # Test multiple additions
        expected = 16
        actual = mymodule.Calculator.add_multiple_numbers(self.numberOne, self.numberTwo, self.numberThree, self.numberTen)
        self.assertEqual(actual, expected, 'multiple additions failed')

    def test_division(self):
        """
        Tests the correctness of variable instantiation by subtracting with them.
        :return:
        """
        expected = 5
        # Below var should equal 5
        var_to_subtract = mymodule.Calculator.add(self.numberThree, self.numberTwo)
        actual = mymodule.Calculator.subtract(self.numberTen, var_to_subtract)
        self.assertEqual(actual, expected)


# This makes sure the module is ran when called directly (e.g. from the commandline)
if __name__ == '__main__':
    unittest.main()
