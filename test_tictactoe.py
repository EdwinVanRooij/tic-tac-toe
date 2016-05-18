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


# class TestPlayer(unittest.TestCase):
#     """
#     A player participates in a game. A game has exactly two players.
#     """
#     player = None
#
#     def testGetCurrentTurn(self):
#         """
#         Returns the current turn of the player, this is the last one added.
#         :return:
#         """
#         # Reset the player so that the other tests have no effect on this one
#         # todo: the self.player variable won't set it's value to None, wtf?
#         TestPlayer.player = None
#         TestPlayer.player = Player(player_bob_name)
#
#         print(('amount of turns currently:', len(TestPlayer.player.turnHistory)))
#
#         expected = TestPlayer.player.create_turn()
#         actual = TestPlayer.player.get_current_turn()
#         self.assertEqual(expected, actual)
#
#     def testCreateTurn(self):
#         """
#         A player may not have more than 5 turns.
#         :return:
#         """
#         # Reset the player so that the other tests have no effect on this one
#         TestPlayer.player = None
#         TestPlayer.player = Player(player_bob_name)
#
#         expected = 1  # Since there is an existing turn from test A
#         # Test whether or not the turn was added to the history of turns
#         TestPlayer.player.create_turn()
#         actual = len(TestPlayer.player.turnHistory)
#         # Verify that there was a turn added
#         self.assertEqual(expected, actual)
#
#         # Add 3 turns so that we're at 5, we made the first up here
#         for i in range(4):
#             TestPlayer.player.create_turn()
#
#         # At 5 turns now, try to create the sixth one. Should throw exception.
#         with self.assertRaises(TurnsOutOfBoundsError):
#             TestPlayer.player.create_turn()


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


class TestSimpleFoo(unittest.TestCase):
    print('Ran class initialization...')
    foo = 'could'

    def setUp(self):
        print('Ran setup...')
        self.foo = 'would'

    def tearDown(self):
        print('Ran teardown...')
        self.foo = 'canttt'

    def test_z(self):
        print('Ran test 1...')
        self.foo = 'cant'

    def test_f(self):
        print('Ran test 2...')
        print(self.foo)
        self.foo = None
        self.assertEqual(self.foo, None)

# if __name__ == '__main__':
#     unittest.main()
