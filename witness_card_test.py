from witness_card import WitnessCard

def run():
    card = WitnessCard()
    assert card.accusation_value == 7
    assert card.description() == "Worth 7 accusations"

if __name__ == "__main__":
    run()

    print("All tests pass!")
