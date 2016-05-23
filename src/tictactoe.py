#!/usr/bin/env
import os

# Declare variables
turns = []
finished = False

empty = '[   ]'
hit = '[ x ]'


class Turn:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def board():
    """Creates the board"""
    result = []
    for x in range(3):
        result.append([empty] * 3)
    for turn in turns:
        result[turn.y][turn.x] = hit
    return result


def print_board():
    """Prints the board"""
    _board = board()
    for row in _board:
        print(" ".join(row))


def prompt_turn():
    print('It\'s your turn, {}.'.format(name))
    x = input('Location x: ')
    y = input('Location y: ')
    turns.append(Turn(int(x) - 1, int(y) - 1))


def check_winner():
    # Check for straight rows
    for i in range(0, 4):
        in_a_row = 0
        for turn in turns:
            if turn.x == i:
                in_a_row += 1
        if in_a_row == 3:
            return True

        in_a_row = 0
        for turn in turns:
            if turn.y == i:
                in_a_row += 1
        if in_a_row == 3:
            return True

    # Check for diagonal lines
    in_a_row = 0
    for turn in turns:
        # Check for top-left to bottom-right
        if turn.x == 0 and turn.y == 0:
            in_a_row += 1
        if turn.x == 1 and turn.y == 1:
            in_a_row += 1
        if turn.x == 2 and turn.y == 2:
            in_a_row += 1
        if in_a_row == 3:
            return True

    in_a_row = 0
    for turn in turns:
        # Check for top-right to bottom-left
        if turn.x == 2 and turn.y == 0:
            in_a_row += 1
        if turn.x == 1 and turn.y == 1:
            in_a_row += 1
        if turn.x == 0 and turn.y == 2:
            in_a_row += 1
        if in_a_row == 3:
            return True


# Start the game
print()
print('Welcome to Tic-Tac-Toe!')
print()
print('What is your name?')
name = input('Name: ')
print()

print('Let\'s start!')
print()

while finished is False:
    os.system('clear')
    print()
    print_board()
    print()
    prompt_turn()
    if check_winner():
        finished = True

print('\nCongratulations!\n{} has won the game!'.format(name))
