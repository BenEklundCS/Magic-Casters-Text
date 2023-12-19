""" Functions imports """
from functions import game_over, roll_d20, random_letter, check_roll # Utility functions
from functions import slow_print, clear_terminal_line # Terminal interactions

LENGTH_OF_PUZZLE = 4

def memory_puzzle():
    """ Puzzle to test the players memory, forward path on crossroads """
    slow_print("You come across a stone room, with runes on the walls.")
    slow_print("Another adventurer's skeleton lies dead on the floor, looted long ago.")
    # Player rolls a perception check
    roll = roll_d20()
    check_roll(roll, "perception")
    if roll > 10:
        slow_print("You realize this must be an ancient runic memory puzzle.")
    else:
        slow_print("You fail to determine the meaning of this room. Maybe you can still survive?")
    # While puzzle is not completed...
    completed = False
    chars = []
    failures = 0
    while completed is False and len(chars) <= LENGTH_OF_PUZZLE:
        # Generate a random letter and add it to the chars buffer
        letter = random_letter()
        chars.append(letter)
        # Print the letter to the terminal
        print(letter)
        user_input = input()
        # If the users input does not match the full buffer, add a failure
        if user_input != ''.join(chars):
            slow_print(f"\rThat is incorrect! You have {3-failures} more tries....................")
            failures = failures+1
            # Call game_over() if they've failed too many times
            if failures == 4:
                game_over()
            # Clear the chars buffer
            chars.clear()
        # Otherwise, the users input matches the full buffer
        else:
            slow_print("\rCorrect!")
            # If the full buffer is equal to the LENGTH_OF_PUZZLE constant, they've won!
            if len(chars) == LENGTH_OF_PUZZLE:
                completed = True
                break
        # Clear the terminal a few times
        clear_terminal_line() # clear output (correct/incorrect)
        clear_terminal_line() # clear player input
        clear_terminal_line() # clear given letter
    # Exit puzzle with a true return
    return completed
