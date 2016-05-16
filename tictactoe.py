#!/usr/bin/env
from datetime import datetime


# Define classes
class Game:
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """
    winner = None
    createdAt = None
    endedAt = None

    def __init__(self):
        self.createdAt = datetime.now()


class Player:
    """
    A player participates in a game. A game has exactly two players.
    """
    turns = 5
    turnHistory = []
    name = 'Unset name in \'Player\' class'

    def create_turn(self):
        self.turnHistory.append(Turn())


class Turn:
    """
    A turn in a game. A turn is created and executed by a player.
    A turn contains meta data about the turn, like when the player created and executed the turn.
    """
    location = None
    createdAt = None
    executedAt = None

    def __init__(self):
        self.createdAt = datetime.now()

    def execute_turn(self, x, y):
        self.location = Location(x, y)

    def get_time_taken(self):
        return (self.createdAt-self.executedAt).total_seconds()


class Location:
    """
    The location of the X or O placed by the player.
    """
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


print("Starting program...")

print("...end of program.")
