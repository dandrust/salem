from game import Game

if __name__ == "__main__":
    game = Game(2)
    assert game.not_a_witch_cards_required() == 18
    assert game.witch_cards_required() == 1
    assert game.constable_cards_required() == 1

    game = Game(5)
    assert game.not_a_witch_cards_required() == 23
    assert game.witch_cards_required() == 1
    assert game.constable_cards_required() == 1

    game = Game(8)
    assert game.not_a_witch_cards_required() == 29
    assert game.witch_cards_required() == 2
    assert game.constable_cards_required() == 1

    game = Game(11)
    assert game.not_a_witch_cards_required() == 30
    assert game.witch_cards_required() == 2
    assert game.constable_cards_required() == 1

    game = Game(12)
    assert game.not_a_witch_cards_required() == 33
    assert game.witch_cards_required() == 2
    assert game.constable_cards_required() == 1

    print("All tests pass!")