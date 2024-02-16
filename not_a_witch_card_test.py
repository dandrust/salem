from not_a_witch_card import NotAWitchCard
from tryal_card import TryalCard

def run():
    card = NotAWitchCard()
    assert isinstance(card, TryalCard)
    assert str(card) == "Not a Witch"



if __name__ == "__main__":
    run()

    print("All tests pass!")