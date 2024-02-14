from accusation_card_test import run as run_accusation_card_tests
from evidence_card_test import run as run_evidence_card_tests
from witness_card_test import run as run_witness_card_tests

if __name__ == "__main__":
    run_accusation_card_tests()
    run_evidence_card_tests()
    run_witness_card_tests()

    print("All tests pass!")