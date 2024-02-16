from player import Player
from witch_card import WitchCard
from not_a_witch_card import NotAWitchCard
from constable_card import ConstableCard
from accusation_card import AccusationCard

def run():
    witch_card = WitchCard()
    not_a_witch_card = NotAWitchCard()
    constable_card = ConstableCard()
    decoy_card = AccusationCard()

    player = Player("Dan")

    # TODO 3: has_been_a_witch is set to false initially
    assert player.has_been_a_witch == False

    # TODO 2: responds to assign_tryal_cards, recalls state and order
    player.assign_tryal_cards(witch_card, not_a_witch_card, constable_card)
    assert player.tryal_cards[0] == witch_card
    assert player.tryal_cards[1] == not_a_witch_card
    assert player.tryal_cards[2] == constable_card

    # TODO 3: has_been_a_witch is set to true when witch card has been assigned
    assert player.has_been_a_witch == True

    # TODO 2: assigning a non-tryal card raises an error
    another_player = Player("Kate")
    try:
        another_player.assign_tryal_cards(witch_card, not_a_witch_card, decoy_card)
        assert False # If we get here that means calling assign_tryal_card with an accusation card DIDN'T raise an error, FAIL!
    except TypeError as _:
        pass

    # TODO 3: has_been_a_witch is NOT set to true when a witch card isn't passed
    another_player.assign_tryal_cards(not_a_witch_card, not_a_witch_card, not_a_witch_card)

if __name__ == "__main__":
    run()

    print("All tests pass!")


        
    

