#!/usr/bin/env

from src.tictactoe import *
import time
import sys

# Flat row 'enum'
FlatRow = ['NONE', 'TOP', 'BOTTOM']
NONE = 0
TOP = 1
BOTTOM = 2

# Delay 'enum'
Delay = [0.03, 0.0075]
SLOW = 0
FAST = 1


def print_board():
    """
    Prints the game board
    :return:
    """
    print_three_lines(FlatRow[TOP])
    print_three_lines(FlatRow[TOP], FlatRow[BOTTOM])
    print_three_lines(FlatRow[BOTTOM])


def print_three_lines(*flat_row):
    """
    Prints three lines with an optional row before and/or after.
    The row before and/or after closes or opens a tic-tac-toe row.
    :param flat_row: prints a opening/closing line
    :return:
    """
    # Print a line before the row
    if flat_row.__contains__(FlatRow[TOP]):
        print_line('-', 26)

    tab = '\t'
    border = '|'
    for i in range(3):
        print(border, tab, border, tab, border, tab, border)

    # Print a closing line
    if flat_row.__contains__(FlatRow[BOTTOM]):
        print_line('-', 26)


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
        sys.stdout.write()
    print("".join(string_list))


def delay_print(string, delay):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Delay[delay])


# Start the game!
game = Game()

# Greet the user
delay_print('Greetings!\nLet\'s play Tic-Tac-Toe!\n\nFirst of all, what\'s your name?', SLOW)

player_one_name = input()

delay_print('{}\'s a nice name! Now, what about player two?'.format(player_one_name), SLOW)

player_two_name = input()

game.add_player(player_one_name)
game.add_player(player_two_name)

print_board()
