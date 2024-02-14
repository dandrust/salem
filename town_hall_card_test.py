from town_hall_card import TownHallCard

if __name__ == "__main__":
    card = TownHallCard("Will Griggs", "Physician", 47)
    assert card.name == "Will Griggs"
    assert card.occupation == "Physician"
    assert card.age == 47
    assert str(card) == "Will Griggs (47), Physician"

    print("All tests pass!")