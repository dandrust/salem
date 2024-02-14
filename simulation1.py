"""
    Task 5

    Objectives: Instantiate classes and call methods
                Use tuples to instantiate objects with * deconstruction
                Use for loops and ranges to repeat tasks
                Use the `random` module to simulate shuffling cards
                Use lists to organize mutable collections

    TODO: Write a script that simulates game setup for NUM_PLAYERS players. Create
    a Player instance for each player and assign the player a random Town Hall card.
    You should use the TOWN_HALL_CARD_DATA in `static_data.py` to setup all possible
    Town Hall cards. Then, "shuffle" the cards and "deal" one to each player! Finally,
    print a summary of who's playing and which character they've been assigned!

    This task includes a random element so a test script wouldn't be reliable, so you'll
    need to test this on your own by observing printed output.
    Some "gotchas" to consider:
        * Will player names appear in the game exactly once?
        * Will a given town hall cards be dealt to only one player?
"""

import random
from static_data import TOWN_HALL_CARD_DATA
from player import Player
from town_hall_card import TownHallCard

NUM_PLAYERS = 3 # You can change this!

# Setup Players
player_candidates = [
    "Dan", "Kate", "Lindsey", "Mitch", "Meredith", "Tre", "Rachel",
    "Tommy", "Larissa", "Elaine", "Bob", "Sue", "Bruce", "Marcia", "Mickey"
]

random.shuffle(player_candidates)

players = []

for _ in range(NUM_PLAYERS):
    players.append(Player(player_candidates.pop()))

# Setup Town Hall cards
town_hall_cards = []

for card_data in TOWN_HALL_CARD_DATA:
    town_hall_cards.append(TownHallCard(*card_data))

random.shuffle(town_hall_cards)

# "Deal" cards to players, print player information
for player in players:
    card = town_hall_cards.pop()
    player.assign_town_hall_card(card)
    print(str(player))
