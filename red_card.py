"""
    Task 6

    Objectives: Use inheritance to model type/subtype relationships
                Use class attributes to set data applicable to all instances
                Use `import ... from ...`

    TODO: Use the RedCard class below as a parent for three new classes to
    represent the types of red card that exist: WitnessCard, EvidenceCard,
    and AccusationCard. Each subclass should live in it's own file. Subclasses
    should override the parent's `accusation_value` attribute with the 
    appropriate value. Subclasses should also implement the `description` 
    method with the appropriate card description, eg:
        "Worth 7 accusations"

    Run `python3 red_card_test.py` to run the tests and confirm your implementation is correct.
"""

class RedCard:
    accusation_value = 0

    def description(_self):
        raise NotImplementedError("Subclasses must implement description")