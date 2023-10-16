""" Module import """
from os import system
from functions import slow_print, color, clear_terminal_line

def title():
    """ Title screen """
    print(color("##################################################", "blue"))
    print(color("#                                                #", "blue"))
    print(color("#            --- Magic Casters ---               #", "blue"))
    print(color("#                                                #", "blue"))
    print(color("#          A text RPG by Ben Eklund              #", "blue"))
    print(color("#                                                #", "blue"))
    print(color("##################################################", "blue"))

def main_menu():
    """ Main menu """
    print(color("Options: ", "white"))
    print(color("1. Start ", "green"))
    print(color("2. Exit  ", "red"))
    # Handle input w/ valid options
    options = ['1', '2']
    user_input = ""
    slow_print(f"Please make a selection: {options}")
    while user_input not in options:
        user_input = input()
        clear_terminal_line()
    system("clear")
    return True if user_input == '1' else False

def mini_header():
    """ Mini version of title header """
    print(color("##################################################", "blue"))
    print(color("#            --- Magic Casters ---               #", "blue"))
    print(color("#          A text RPG by Ben Eklund              #", "blue"))
    print(color("##################################################", "blue"))
