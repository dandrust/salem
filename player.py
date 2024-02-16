"""
    Task 4

    Objective: Use a python class to represent a game player
               Allow a player to be assigned a town hall card
               Use the special __str__ method to print instance state, and the state of embeded instances

    TODO: Implement a Player class to represent a game player.  The class should be initialized with the player's
          name.  The class should also implement an `assign_town_hall_card` method that "saves" the town hall card
          to the player instance.  Finally, when printed the instance should read, eg:
            "Kate is playing as Sarah Good (39), Beggar"

    See `player_test.py` for the expected interface of the Player class

    Run `python3 player_test.py` to run the tests and confirm your implementation is correct.
"""

from player_task_7 import PlayerTask7 # Ignore this until you reach task 7

class Player(PlayerTask7):
    def __init__(self, name):
        super().__init__()
        self.name = name        
    
    def assign_town_hall_card(self, card):
        self.town_hall_card = card
      
    def __str__(self):
        return f"{self.name} is playing as {self.town_hall_card}"
