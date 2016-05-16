#!/usr/bin/env
import unittest
from tictactoe import *


class TestGame(unittest.TestCase):
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """
    game = None

    def setUp(self):
        self.game = Game()

    def test_createdAt(self):
        """
        Tests whether or not the game has received a Date object on creation.
        :return:
        """
        self.assertIsNotNone(self.game.createdAt, 'createdAt variable was not instantiated')

    def test_add_player(self):
        """
        Adds a player to the game. The game may not contain more than two players.
        Returns true if adding the player was successful.
        :return:
        """
        # Adding the first player should succeed.
        self.assertTrue(self.game.add_player('Bob'))
        # Adding the second player should also succeed.
        self.assertTrue(self.game.add_player('Alice'))
        # Adding a third player should not succeed as the max is 2.
        with self.assertRaises(PlayerOutOfBoundsError):
            self.game.add_player('Hank')


class TestPlayer(unittest.TestCase):
    """
    A player participates in a game. A game has exactly two players.
    """
    name = 'Bob'
    player = None

    def setUp(self):
        self.player = Player(self.name)

    def test_create_turn(self):
        """
        A player may not have more than 5 turns.
        :return:
        """
        expected = 1
        # Test whether or not the turn was added to the history of turns
        self.player.create_turn()
        actual = len(self.player.turnHistory)
        # Verify that there was a turn added
        self.assertEqual(expected, actual)

        # Test if we can go over 5 turns
        for i in range(4):
            self.player.create_turn()
        # At 5 turns now, try to create the sixth one. Should throw exception.
        with self.assertRaises(TurnsOutOfBoundsError):
            self.player.create_turn()


# This makes sure the module is ran when called directly (e.g. from the commandline)
if __name__ == '__main__':
    unittest.main()
