from functions import game_over, slow_print, d20, random_letter

def memory_puzzle():
    """ Puzzle to test the players memory, forward path on crossroads """
    slow_print("You come across a stone room, with runes on the walls.")
    slow_print("Another adventurer's skeleton lies dead on the floor, looted long ago.")
    roll = d20()
    slow_print(f"... you roll a {roll} for perception ...")
    if roll > 10:
        slow_print("You realize this must be an ancient runic memory game - and prepare yourself for its start.")
    else:
        slow_print("You fail to determine the meaning of this room. Maybe you can catch on in time to survive?")
    
    completed = False
    chars = []
    failures = 0
    while completed is False and len(chars) <= 7:
        letter = random_letter()
        chars.append(letter)
        print(letter)
        user_input = input()
        if user_input != ''.join(chars):
            slow_print(f"That is incorrect! You have {3-failures} more tries.")
            failures = failures+1
            if failures == 3:
                game_over()
            chars.clear()
        else:
            slow_print("Correct!")
            if len(chars) == 7:
                completed = True
    return completed
    


   


    