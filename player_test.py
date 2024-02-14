from player import Player
from town_hall_card import TownHallCard

if __name__ == "__main__":
    player = Player("Kate")
    assert player.name == "Kate"

    card = TownHallCard("Sarah Good", "Beggar", 39)
    player.assign_town_hall_card(card)

    assert player.town_hall_card == card
    assert str(player) == "Kate is playing as Sarah Good (39), Beggar"

    print("All tests pass!")