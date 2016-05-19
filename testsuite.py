#!/usr/bin/env
import unittest

from tests import test_tictactoe


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestGame))
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestPlayer))
    test_suite.addTest(unittest.makeSuite(test_tictactoe.TestTurn))
    # test_suite.addTest(unittest.makeSuite(test_tictactoe.TestSimpleFoo))
    return test_suite


runner = unittest.TextTestRunner()
runner.run(suite())
