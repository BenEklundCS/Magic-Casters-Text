""" Modules """
import time
import random
import sys
import string # used for string.ascii_letters

# Color

END_COLOR = '\033[0m'
RED_COLOR = '\033[1;31;49m'
GREEN_COLOR = '\033[1;32;49m'
BLUE_COLOR = '\033[1;34;49m'
YELLOW_COLOR = '\033[1;33;49m'
WHITE_COLOR = '\033[1;37;49m'
GRAY_COLOR = '\033[0;37;49m'

def color(text, clr):
    """ Used to color terminal output """
    if clr == "red":
        return RED_COLOR + text + END_COLOR
    elif clr == "green":
        return GREEN_COLOR + text + END_COLOR
    elif clr == "blue":
        return BLUE_COLOR + text + END_COLOR
    elif clr == "yellow":
        return YELLOW_COLOR + text + END_COLOR
    elif clr == "gray":
        return GRAY_COLOR + text + END_COLOR
    else:
        return WHITE_COLOR + text + END_COLOR

# Dice
def roll_d2():
    """ d2 die """
    return random.randint(1, 2)

def roll_d4():
    """ d4 die """
    return random.randint(1, 4)

def roll_d6():
    """ d6 die """
    return random.randint(1, 6)

def roll_d8():
    """ d8 die"""
    return random.randint(1, 8)

def roll_d20():
    """ d20 die """
    return random.randint(1, 20)

# Random letter

def random_letter():
    """ Returns a random letter in the alphabet """
    return random.choice(string.ascii_letters)

# Printing
def slow_print(text):
    """ take text and print it character by character """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    print()

def slower_print(text):
    """ take text and print it character by character """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def print_attack(self, monster, roll, attack_name):
    """ Print player attack """
    raw_damage = roll + self.attack
    total_damage = raw_damage - monster.defense
    slow_print(f"You rolled a {roll} for your {attack_name} attack for {raw_damage} damage.")
    slow_print(f"{monster.name} blocked {monster.defense} damage, for {total_damage} total damage.")
    monster.health = monster.health - total_damage
    slow_print(f"The {monster.name}'s health is now {monster.health}")

def clear_terminal_line():
    """ uses sys to move up a line and clear """
    sys.stdout.write("\033[F") # back to previous line
    sys.stdout.write("\033[K") # clear line

def line_break():
    """ Line break in terminal """
    print("\n")
    print(color("##################################################################################################################################", "gray"))
    print(color("##################################################################################################################################", "gray"))
    print("\n")

# Game over 
def game_over():
    """ End game """
    print(color("##################################################################################################################################", "red"))
    print(color("#                                            GAME OVER                                                                           #", "red"))
    print(color("##################################################################################################################################", "red"))
    print("Thank you for playing! :)")
    input() # Hold user at game over until input
    exit()

# Fight loop
def fight(player, monster, player_turn):
    """ Fight loop """

    options = ["slash", "slam", "info", "pass"]
    user_input = ""
    # If monsters turn, attack the player
    if player_turn is False:
        monster.choose_attack(player)
    # If the player is dead, call gameOver
    if player.check_death() is True:
        game_over()
    while user_input not in options:
        line_break()
        slow_print("It is your turn to attack.")
        slow_print(f"Options: {options}")
        user_input = input()
        clear_terminal_line()
        # Possible user attacks
        if user_input == "slash":
            player.slash(monster)
        elif user_input == "slam":
            player.slam(monster)
        # User utility options
        elif user_input == "info":
            player.info()
            user_input = ""
            continue
        elif user_input == "pass":
            player.pass_turn()
        # Error handling
        else:
            slow_print("Invalid option. Please enter a valid attack!")
            continue
        # Did player action kill the monster?
        if monster.check_death(player) is True:
            return True
        # Attack the player
        monster.choose_attack(player)
        # Did the player die?
        if player.check_death() is True:
            game_over()
        # Reset for next iteration
        user_input = ""
    return False

def check_roll(roll, check):
    """ Formats roll and type into slow printed f-string """
    slow_print(f"... you roll a {roll} for {check}...")

def validate_input(options):
    """ Input validation """
    print(f"Options: {options}")
    user_input = input()
    while user_input not in options:
        print("Invalid input!")
        user_input = input()
    return user_input
