#!/usr/bin/env
from datetime import datetime


class Game:
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """
    winner = None
    createdAt = None
    endedAt = None

    def __init__(self):
        global createdAt
        createdAt = datetime.now()
        print(createdAt)

game = Game()

