#!/usr/bin/env

# Declare constants
amountOfColumns = 3
amountOfRows = 3


def write_board():
    """
    Writes the Tic-Tac-Toe board
    :return:
    """
    print_top_row()
    for i in range(amountOfColumns):
        print_row(True)

def print_top_row():


def print_row(is_top_row=False, is_middle_row=False, is_bottom_row=False):
    """
    Prints a single row on the board
    :param is_top_row: boolean, if true we'll write the top row
    :param is_middle_row: boolean, if true we'll write a middle row
    :param is_bottom_row: boolean, if true we'll write the bottom row
    :return:
    """
    if is_top_row:
        pass
    if is_middle_row:
        pass
    if is_bottom_row:
        pass


def start_game():
    """
    Starts the game
    :return:
    """
    print('Starting game...')
    end_game()


def end_game():
    """
    Ends the game
    :return:
    """
    print('...end of game.')

start_game()
