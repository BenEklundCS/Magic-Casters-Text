from functions import game_over

def word_puzzle():
    """ Word puzzle placeholder """
    print("A wizard would carry one proudly.")
    user_input = input()
    failures = 0
    while user_input != "staff":
        print(f"That is incorrect! You have {3-failures} more tries.")
        if failures >= 3:
            game_over()
        failures += 1
        user_input = input()
    return True
    