#!/usr/bin/env

from src.tictactoe import *


def print_board():
    """
    Prints the game board
    :return:
    """
    print_line('-', 10)


def print_line(string, times):
    """
    Prints a flexible line
    :param string: the string to repeat
    :param times: amount of times to repeat
    :return:
    """
    string_list = []
    for i in range(times):
        string_list.append(string)
    print(*string_list, end='\n')


game = Game()

bob_name = 'Bob'
alice_name = 'Alice'

game.add_player(bob_name)
game.add_player(alice_name)

print_board()
