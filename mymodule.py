#!/usr/bin/env
import random


# Define classes
class Calculator:
    """
    A simple calculator class as part of my testing template.
    """
    id = None

    def __init__(self):
        """
        Initiates own variables
        """
        self.__generate_id()

    def get_id(self):
        """
        Returns the ID of current object
        :return: an integer ID
        """
        return self.id

    def __generate_id(self):
        """
        Generate a complex ID for an instance of this class
        :return:
        """
        self.id = random.randrange(1000, 1500)

    @staticmethod
    def subtract(first, second):
        """
        Adds two numbers
        :param first: number to subtract from
        :param second: number to subtract
        :return: an integer result of the subtraction
        """
        return first - second

    @staticmethod
    def add(first, second):
        """
        Adds two numbers and returns the result
        :param first: first number to add
        :param second: second number to add
        :return: the integer result of the calculation
        """
        return first + second

    @staticmethod
    def add_multiple_numbers(first, *other_numbers):
        """
        Adds three numbers up to an integer
        :param first: the number to start with
        :param arguments: all numbers to add the first number up with
        :return: an integer result of the calculation
        """
        result = first
        for number in other_numbers:
            # Use the add method of this class to add the result up
            result = Calculator.add(result, number)
        return result
