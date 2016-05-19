#!/usr/bin/env
import time
import unittest

from src.tictactoe import *

player_bob_name = 'Bob'
player_alice_name = 'Alice'
player_hank_name = 'Hank'
delay = 0.2


class TestGame(unittest.TestCase):
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """

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

    def setUp(self):
        self.game = Game()
        self.game.add_player(player_bob_name)

    def testGetPlayerNumber(self):
        """
        Must be either 1 or 2
        :return:
        """
        self.game.add_player(player_bob_name)

    def testGetCurrentTurn(self):
        """
        Returns the current turn of the player, this is the last one added.
        :return:
        """
        expected = self.game.players[0].create_turn()
        actual = self.game.players[0].get_current_turn()
        self.assertEqual(expected, actual, 'Just added turn is not the created turn')

    def testCreateTurn(self):
        """
        Test whether or not a turn is actually created
        :return:
        """
        expected = 1
        # Test whether or not the turn was added to the history of turns
        self.game.players[0].create_turn()
        actual = len(self.game.players[0].turnHistory)
        # Verify that there was a turn added
        self.assertEqual(expected, actual, 'There was not exactly one turn added')

    def testCreateTurnMax(self):
        """
        A player may not have more than 5 turns.
        :return:
        """
        # Add 5 turns
        for i in range(5):
            self.game.players[0].create_turn()

        # At 5 turns now, try to create the sixth one. Should throw exception.
        with self.assertRaises(TurnOutOfBoundsError):
            self.game.players[0].create_turn()


class TestTurn(unittest.TestCase):
    """
    A turn in a game. A turn is created and executed by a player.
    A turn contains meta data about the turn, like when the player created and executed the turn.
    """

    def setUp(self):
        self.game = Game()
        self.game.add_player(player_bob_name)
        self.player = self.game.players[0]
        self.player.create_turn()

    def testExecuteTurn(self):
        """
        The user actively executes the turn, choosing a position on the board.
        executedAt variable should be filled here
        createdAt should be tested as well, but on the create turn already
        :return:
        """
        turn = self.player.get_current_turn()
        # Should work, 3 is the last index of the board
        turn.execute_turn(3, 3)
        # Should work as well, 1 is the first index on the board
        second_turn = self.player.create_turn()
        second_turn.execute_turn(1, 1)

    def testInvalidTurnsNegative(self):
        """
        :param x: horizontal index value of the board, must be either 1, 2 or 3
        :param y: vertical index value of the board, must be either 1, 2 or 3
        """
        # The numbers below 1 and above 3 should raise an exception
        with self.assertRaises(OutOfBoardError):
            # Loop from 0 to -3
            for i in range(0, -3, -1):
                turn = self.player.create_turn()
                turn.execute_turn(i, i)

    def testInvalidTurnsPositive(self):
        """
        :param x: horizontal index value of the board, must be either 1, 2 or 3
        :param y: vertical index value of the board, must be either 1, 2 or 3
        """
        # The numbers below 1 and above 3 should raise an exception
        with self.assertRaises(OutOfBoardError):
            # Loop from 4 to 7
            for i in range(4, 7, 1):
                turn = self.player.create_turn()
                turn.execute_turn(i, i)

    def testDates(self):
        """
        createdAt is created on turn creation
        executedAt is created on turn completion
        :return:
        """
        before = datetime.now()
        # Generate a quick delay
        time.sleep(delay)
        new_turn = self.player.create_turn()
        time.sleep(delay)
        after = datetime.now()
        # Now check whether or not the new turn was after the before & before the after
        if new_turn.createdAt <= before or new_turn.createdAt >= after:
            self.fail('The creation of the turn has set an invalid createdAt')

        before_execution = datetime.now()
        # Generate a quick delay
        time.sleep(delay)
        new_turn.execute_turn(2, 2)
        # Generate a quick delay
        time.sleep(delay)
        after_execution = datetime.now()
        # Check whether or not the execution happened after the before and before the after
        if new_turn.executedAt <= before_execution or new_turn.executedAt >= after_execution:
            self.fail('The execution of the turn has set an invalid executedAt')


class TestSimpleFoo(unittest.TestCase):
    foo = None
    print('Ran class initialization:\t', foo)

    def setUp(self):
        self.foo = 'setup'
        print('Ran setup:\t', self.foo)

    def tearDown(self):
        self.foo = None
        print('Ran teardown:\t', self.foo)

    def test_a(self):
        self.foo = 'test_a'
        print('Ran test [A]:\t', self.foo)
        self.assertEqual(self.foo, 'test_a')

    def test_b(self):
        self.foo = 'test_b'
        print('Ran test [B]:\t', self.foo)
        self.assertEqual(self.foo, 'test_b')

    def test_c(self):
        self.foo = 'test_c'
        print('Ran test [C]:\t', self.foo)
        self.assertEqual(self.foo, 'test_c')

# if __name__ == '__main__':
#     unittest.main()
