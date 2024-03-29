"""
    Task 1

    Objectives: Use control-flow structures to calculate output based on input

    TODO: Implement the following functions. Each function should take in a single parameter, 
    player_count, and return the number of cards required for that quantity of players. If the 
    player_count is invalid, return None. See game rules, p. 3

    Run `python3 games_setup_script.py` to run the tests and confirm your implementation is correct.
"""

def not_a_witch_cards_required(player_count):
    return None

def witch_cards_required(player_count):
    return None

def constable_cards_required(player_count):
    return None

# Tests
if __name__ == "__main__":
    # not a witch cards
    assert not_a_witch_cards_required(-1) == None
    assert not_a_witch_cards_required(0) == None
    assert not_a_witch_cards_required(1) == None
    assert not_a_witch_cards_required(2) == 18
    assert not_a_witch_cards_required(3) == 18
    assert not_a_witch_cards_required(4) == 18
    assert not_a_witch_cards_required(5) == 23
    assert not_a_witch_cards_required(6) == 27
    assert not_a_witch_cards_required(7) == 32
    assert not_a_witch_cards_required(8) == 29
    assert not_a_witch_cards_required(9) == 33
    assert not_a_witch_cards_required(10) == 27
    assert not_a_witch_cards_required(11) == 30
    assert not_a_witch_cards_required(12) == 33
    assert not_a_witch_cards_required(13) == None
    assert not_a_witch_cards_required(100) == None

    # witch cards
    assert witch_cards_required(-1) == None
    assert witch_cards_required(0) == None
    assert witch_cards_required(1) == None

    for i in range(2, 5):
    assert witch_cards_required(i) == 1

    for i in range(6, 12):
    assert witch_cards_required(i) == 2

    assert witch_cards_required(13) == None
    assert witch_cards_required(100) == None

    # constable cards
    assert constable_cards_required(-1) == None
    assert constable_cards_required(0) == None
    assert constable_cards_required(1) == None

    for i in range(2, 13):
    assert constable_cards_required(i) == 1

    assert constable_cards_required(13) == None
    assert constable_cards_required(100) == None

    print("All tests pass!")
