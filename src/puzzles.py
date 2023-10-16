""" Functions imports """
from functions import game_over, roll_d20, random_letter, check_roll # Utility functions
from functions import slow_print, clear_terminal_line # Terminal interactions

LENGTH_OF_PUZZLE = 4

def memory_puzzle():
    """ Puzzle to test the players memory, forward path on crossroads """
    slow_print("You come across a stone room, with runes on the walls.")
    slow_print("Another adventurer's skeleton lies dead on the floor, looted long ago.")
    roll = roll_d20()
    check_roll(roll, "perception")
    if roll > 10:
        slow_print("You realize this must be an ancient runic memory puzzle.")
    else:
        slow_print("You fail to determine the meaning of this room. Maybe you can still survive?")
    completed = False
    chars = []
    failures = 0
    while completed is False and len(chars) <= LENGTH_OF_PUZZLE:
        letter = random_letter()
        chars.append(letter)
        print(letter)
        user_input = input()
        if user_input != ''.join(chars):
            slow_print(f"\rThat is incorrect! You have {3-failures} more tries....................")
            failures = failures+1
            if failures == 4:
                game_over()
            chars.clear()
        else:
            slow_print("\rCorrect!")
            if len(chars) == LENGTH_OF_PUZZLE:
                completed = True
                break
        clear_terminal_line() # clear output (correct/incorrect)
        clear_terminal_line() # clear player input
        clear_terminal_line() # clear given letter
    return completed
