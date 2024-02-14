from evidence_card import EvidenceCard

def run():
    card = EvidenceCard()
    assert card.accusation_value == 3
    assert card.description() == "Worth 3 accusations"

if __name__ == "__main__":
    run()
    
    print("All tests pass!")