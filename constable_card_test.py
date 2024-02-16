from constable_card import ConstableCard
from tryal_card import TryalCard

def run():
    card = ConstableCard()
    assert isinstance(card, TryalCard)
    assert str(card) == "Constable"



if __name__ == "__main__":
    run()

    print("All tests pass!")