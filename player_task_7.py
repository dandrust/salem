from tryal_card import TryalCard
from witch_card import WitchCard

class PlayerTask7:
    def __init__(self):
        self.has_been_a_witch = False
        self.tryal_cards = []

    def assign_tryal_cards(self, card1, card2, card3):
        if not isinstance(card1, TryalCard) or not isinstance(card2, TryalCard) or not isinstance(card3, TryalCard):
            raise TypeError("TryalCard expected") 

        self.tryal_cards = [card1, card2, card3]
        
        if type(card1) == WitchCard or type(card2) == WitchCard or type(card3) == WitchCard:
            self.has_been_a_witch = True
