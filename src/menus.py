""" Module import """
from os import system
from functions import slow_print, color, clear_terminal_line

def title():
    """ Title screen """
    print(color(r"##################################################################################################################################", "blue"))
    print(color(r"#                         _      ____  _____ _  ____    ____  ____  ____  _____  _____ ____  ____                                #", "blue"))
    print(color(r"#                        / \__/|/  _ \/  __// \/   _\  /   _\/  _ \/ ___\/__ __\/  __//  __\/ ___\                               #", "blue"))
    print(color(r"#                        | |\/||| / \|| |  _| ||  /    |  /  | / \||    \  / \  |  \  |  \/||    \    A text adventure by        #", "blue"))
    print(color(r"#                        | |  ||| |-||| |_//| ||  \_   |  \__| |-||\___ |  | |  |  /_ |    /\___ |          Ben Eklund           #", "blue"))
    print(color(r"#                        \_/  \|\_/ \|\____|\_/\____/  \____/\_/ \|\____/  \_/  \____|\_/\_|\____/                               #", "blue"))
    print(color(r"#                                                                                                                                #", "blue"))
    print(color(r"##################################################################################################################################", "blue"))

def main_menu():
    """ Main menu """
    print(color("Options: ", "white"))
    print(color("1. Start ", "green"))
    print(color("2. Exit  ", "red"))
    # Handle input w/ valid options
    options = ['start', 'end']
    user_input = ""
    slow_print(f"Please make a selection: {options}")
    while user_input not in options:
        user_input = input()
        clear_terminal_line()
    system("clear")
    return True if user_input == 'start' else False

def mini_header():
    """ Mini version of title header """
    print(color("##################################################################################################################################", "blue"))
    print(color("#                                                  --- Magic Casters ---                                                         #", "blue"))
    print(color("##################################################################################################################################", "blue"))
