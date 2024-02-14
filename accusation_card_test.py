from accusation_card import AccusationCard

def run():
    card = AccusationCard()
    assert card.accusation_value == 1
    assert card.description() == ""

if __name__ == "__main__":
    run()

    print("All tests pass!")
