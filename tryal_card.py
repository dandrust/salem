"""
    Task 7

    Objectives: Use inheritance to model type/subtype relationships
                Use classes to represent types
                Use `import ... from ...`
                Select a data type based on requirements and constraints
                Use `type()` for detecting class
                Use `isinstance()` for detecting ancestry
                Use instance methods to store state
                Exposure to `pass` keyword

    TODO 1: Similar to task 6, use class inheritance to implement Tryal cards. Tryal
    cards include "Not A Witch", "Witch" and "Constable" cards. Each subclass should
    implement a __str__ function returning it's human-readable type (ie, what's printed
    on the card)

    TODO 2: Modify the Player class to be dealt exactly three Tryal cards in a method
    called assign_tryal_cards. This method should raise an error when a non-Tryal card
    is provided to it. Player instances should remember their Tryal cards. Take extra 
    care when selecting how to store Tryal cards. Keep in mind that they will change 
    throughout the game and their position matters. Choose a Python data type that suits
    these requirements. (Hint: Consider List and Tuple. Which one fits requirements best?)

    TODO 3: Modify the assign_tryal_cards to set an instance variable called
    has_been_a_witch if one of the Tryal cards dealt is a Witch card. Make sure that you
    can call player.has_been_a_witch even if the player hasn't been a witch!

    Run `python3 tryal_card_test.py` and `python3 player_task_7_test.py` to run the tests 
    and confirm your implementation is correct.
"""

class TryalCard:
    pass