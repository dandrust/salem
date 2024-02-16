from witch_card_test import run as run_witch_card_tests
from not_a_witch_card_test import run as run_not_a_witch_card_tests
from constable_card_test import run as run_constable_card_tests
from player_task_7_test import run as run_player_task_7_tests

if __name__ == "__main__":
    run_witch_card_tests()
    run_not_a_witch_card_tests()
    run_constable_card_tests()
    run_player_task_7_tests()

    print("All tests pass!")