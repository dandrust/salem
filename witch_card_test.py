from witch_card import WitchCard
from tryal_card import TryalCard

def run():
    card = WitchCard()
    assert isinstance(card, TryalCard)
    assert str(card) == "Witch"



if __name__ == "__main__":
    run()

    print("All tests pass!")