#!/usr/bin/env
import unittest
from tictactoe import *

player_bob_name = 'Bob'
player_alice_name = 'Alice'
player_hank_name = 'Hank'


class TestGame(unittest.TestCase):
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """
    game = None

    def setUp(self):
        self.game = Game()

    def testCreatedAt(self):
        """
        Tests whether or not the game has received a Date object on creation.
        :return:
        """
        self.assertIsNotNone(self.game.createdAt, 'createdAt variable was not instantiated')

    def testAddPlayer(self):
        """
        Adds a player to the game. The game may not contain more than two players.
        Returns true if adding the player was successful.
        :return:
        """
        # Adding the first player should succeed.
        self.assertTrue(self.game.add_player(player_bob_name))
        # Adding the second player should also succeed.
        self.assertTrue(self.game.add_player(player_alice_name))
        # Adding a third player should not succeed as the max is 2.
        with self.assertRaises(PlayerOutOfBoundsError):
            self.game.add_player(player_hank_name)


class TestPlayer(unittest.TestCase):
    """
    A player participates in a game. A game has exactly two players.
    """
    player = None

    def setUp(self):
        self.player = Player(player_bob_name)
        print('Ran setup... player turns:', len(self.player.turnHistory))

    def tearDown(self):
        self.player.turnHistory = None
        self.player = None

        if self.player is not None:
            print('Player is not None in tearDown')

            if self.player.turnHistory is not None:
                print('turnHistory is not None in tearDown')

        print('Ran teardown... player & turnHistory is None')

    def testGetCurrentTurn(self):
        """
        Returns the current turn of the player, this is the last one added.
        :return:
        """
        print('Starting test a... player turns:', len(self.player.turnHistory))
        expected = self.player.create_turn()
        actual = self.player.get_current_turn()
        self.assertEqual(expected, actual, 'Just added turn is not the created turn')
        print('Ran test a... player turns:', len(self.player.turnHistory))

    def testCreateTurn(self):
        """
        A player may not have more than 5 turns.
        :return:
        """
        print('Starting test b... player turns:', len(self.player.turnHistory))
        expected = 1
        # Test whether or not the turn was added to the history of turns
        self.player.create_turn()
        actual = len(self.player.turnHistory)
        # Verify that there was a turn added
        self.assertEqual(expected, actual, 'There was not exactly one turn added')

        # Add 4 turns so that we're at 5, we made the first up here
        for i in range(4):
            TestPlayer.player.create_turn()

        # At 5 turns now, try to create the sixth one. Should throw exception.
        with self.assertRaises(TurnsOutOfBoundsError, 'should\'ve thrown a TurnsOutOfBoundError'):
            TestPlayer.player.create_turn()

        print('Ran test b... player turns:', len(self.player.turnHistory))


class TestTurn(unittest.TestCase):
    """
    A turn in a game. A turn is created and executed by a player.
    A turn contains meta data about the turn, like when the player created and executed the turn.
    """

    def setUp(self):
        self.player = Player(player_bob_name)
        self.player.create_turn()

        # def testExecuteTurn(self):
        # expected = self.player.turnHistory[0]
        # self.player.
        # actual = self.player.get_current_turn()


# class TestSimpleFoo(unittest.TestCase):
#     foo = None
#     print('Ran class initialization:\t', foo)
#
#     def setUp(self):
#         self.foo = 'setup'
#         print('Ran setup:\t', self.foo)
#
#     def tearDown(self):
#         self.foo = None
#         print('Ran teardown:\t', self.foo)
#
#     def test_a(self):
#         self.foo = 'test_a'
#         print('Ran test [A]:\t', self.foo)
#         self.assertEqual(self.foo, 'test_a')
#
#     def test_b(self):
#         self.foo = 'test_b'
#         print('Ran test [B]:\t', self.foo)
#         self.assertEqual(self.foo, 'test_b')
#
#     def test_c(self):
#         self.foo = 'test_c'
#         print('Ran test [C]:\t', self.foo)
#         self.assertEqual(self.foo, 'test_c')

# if __name__ == '__main__':
#     unittest.main()
