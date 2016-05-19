#!/usr/bin/env

from src.tictactoe import *

game = Game()

bob_name = 'Bob'
alice_name = 'Alice'

bob = Player(bob_name)
alice = Player(alice_name)

game.add_player(bob)
game.add_player(alice)


