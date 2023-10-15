""" Module import """
from functions import slow_print

def title():
    """ Title screen """
    print("##################################################")
    print("#                                                #")
    print("#            --- Magic Casters ---               #")
    print("#                                                #")
    print("#          A text RPG by Ben Eklund              #")
    print("#                                                #")
    print("##################################################")

def main_menu():
    """ Main menu """
    slow_print("Options: ")
    slow_print("1. Start")
    #slow_print("2. Load save") # Huge WIP
    slow_print("2. Exit")
    options = ['1', '2']
    user_input = input()
    while user_input not in options:
        slow_print("Invalid input!")
        user_input = input()
    return True if user_input == '1' else False
