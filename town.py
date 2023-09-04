from functions import slowPrint
from player import *

# Town 
def toTown():
    options = ["inn", "blacksmith", "armoury", "shop"]
    slowPrint("Welcome to town!")
    userInput = ""
    while userInput not in options:
        slowPrint(f"Options: {options}")
        userInput = input()
        if userInput == "inn":
            inn()
        elif userInput == "blacksmith":
            blacksmith()
        elif userInput == "armoury":
            armoury()
        elif userInput == "shop":
            shop()
        else:
            slowPrint("Please enter a valid option.")
        userInput = ""

def inn():
    slowPrint("Dave (Innkeeper): Hi {}, welcome to our humble inn!".format(player.getName()))
def blacksmith():
    slowPrint("Quinn (Blacksmith): Welcome to my blacksmithing shop {}!".format(player.getName()))
def armoury():
    slowPrint("Shelly (Armourer): Welcome to my armoury {}!".format(player.getName()))
def shop():
    return