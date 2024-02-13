"""
  TODO: Use the functions in the `game_setup_script.py` to implement a Game class that we can
  instantiate with the number of players and then call some methods to get the number of cards required

  See `game_test.py` for the expected interface of the Game class.
"""

class Game:
  def __init__(self, player_count):
    self.player_count = player_count

  def not_a_witch_cards_required(self):
    if self.player_count < 2 or self.player_count > 12:
      return None

    match self.player_count:
      case 2 | 3 | 4:
        return 18
      case 5:
        return 23
      case 6 | 10:
        return 27
      case 7:
        return 32
      case 8:
        return 29
      case 9 | 12:
        return 33
      case 11:
        return 30
      

  def witch_cards_required(self):
    if self.player_count < 2 or self.player_count > 12:
      return None

    if self.player_count <= 5:
      return 1
    elif self.player_count > 5:
      return 2

  def constable_cards_required(self):
    if self.player_count < 2 or self.player_count > 12:
      return None

    return 1
