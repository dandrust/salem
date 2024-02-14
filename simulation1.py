"""
    Task 5

    Objectives: Instantiate classes and call methods
                Use tuples to instantiate objects with * deconstruction
                Use for loops and ranges to repeat tasks
                Use the `random` module to simulate shuffling cards

    TODO: Write a script that simulates game setup for NUM_PLAYERS players. Create
    a Player instance for each player and assign the player a random Town Hall card.
    You should use the TOWN_HALL_CARD_DATA in `static_data.py` to setup all possible
    Town Hall cards. Then, "shuffle" the cards and "deal" one to each player! Finally,
    print a summary of who's playing and which character they've been assigned!

    Because this task includes a random element a test script isn't reliable, so none is provided
"""

from random import shuffle
from static_data import TOWN_HALL_CARD_DATA

NUM_PLAYERS: 6 # You can change this!