#!/usr/bin/env
import unittest
import test_tictactoe


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestGame))
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestPlayer))
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestTurn))
    return test_suite


runner = unittest.TextTestRunner()
runner.run(suite())
