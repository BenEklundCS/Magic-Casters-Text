from player import Player
from monsters import Monster, shadowFigure, Goblin
from functions import slowPrint, fight
from town import *

# Initial scene function | introScene() --> crossroadsScene(player)
# player object is generated in introScene() with a user made name
def introScene():
    slowPrint("Welcome to Magic Casters Text!")
    slowPrint("Please enter your name: ")
    name = input()
    player = Player(name, 30, 30, 50, 50, 8, 0, 100)  # name, health, maxHealth, mana, maxMana, attack, defense, gold
    slowPrint("Hi {}, it is a pleasure to meet you!".format(player.getName()))
    slowPrint("I am that handy voice in your head - here to guide you on your journey!")
    slowPrint("These lands are perilous, and there is no coming back from death.")
    slowPrint("Proceed with caution, friend.")
    crossroadsScene(player)

# crossroadsScene is the hub of chapter 1
# Boolean flags in function header to control which paths are taken
def crossroadsScene(player):
    directions = ["left", "right", "forward", "backward"]
    slowPrint("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        slowPrint(f"Options: {directions}")
        userInput = input()
        
        # Left
        if userInput == "left" and player.progress["CH1"]["crossroadsScene"]["leftCompleted"] == False:
            showShadowFigure(player)
        elif userInput == "left" and player.progress["CH1"]["crossroadsScene"]["leftCompleted"] == True:
            slowPrint("You've already gone this way, and there's nothing left to find.")
            userInput = ""

        # Right
        elif userInput == "right" and player.progress["CH1"]["crossroadsScene"]["rightCompleted"] == False:
            goblinFight(player)  # Not yet defined
        elif userInput == "right" and player.progress["CH1"]["crossroadsScene"]["rightCompleted"] == True:
            toTown(player)

        # Forward
        elif userInput == "forward":
            puzzleRoom(player)  # Not yet defined

        # Backward
        elif userInput == "backward":
            slowPrint("You find that this door opens into a wall. Maybe another direction would be better?")
            userInput = ""
        else:
            slowPrint("Please enter a valid option.")

# Intro to shadowFigure fight | showShadowFigure(player) --> shadowFight(player)
# Running sends you back to crossroadsScene()

def showShadowFigure(player):
    options = ["run", "fight"]
    slowPrint("You see a shadowy figure in the distance. It is approaching you.")
    slowPrint("What do you do?")
    userInput = ""
    while userInput not in options:
        slowPrint(f"Options: {options}")
        userInput = input()
        if userInput == "run":
            slowPrint("You run away from the shadowy figure.")
            slowPrint("You find yourself back at the crossroads.")
            crossroadsScene(player)
        elif userInput == "fight":
            slowPrint("You fight the shadowy figure.")
            shadowFight(player)
        else:
            slowPrint("Please enter a valid option.")

# Shadow fight troubleshooting
def shadowFight(player):
    monster = shadowFigure("Shadowy Figure", 50, 100, 15, 0, 50) # name, health, mana, attack, defense, gold
    if fight(player, monster, True) == True:
        del monster
        slowPrint(
            "You also find a key on the shadowy figure's body. Maybe it will be useful later?"
        )
        player.progress["CH1"]["crossroadsScene"]["leftCompleted"] = True 
        crossroadsScene(player)
    return True

# Under dev
def goblinFight(player):
    monster = Goblin("Gob", 25, 50, 10, 0, 100)
    slowPrint("A goblin has appeared!")
    if fight(player, monster, True) == True:
        del monster
        player.progress["CH1"]["crossroadsScene"]["rightCompleted"] = True
        slowPrint("You see the light of a town up ahead, and decide to continue down the trail towards it.")
        toTown(player)
    return True

def toTown(player):
    options = ["inn", "blacksmith", "armoury", "shop", "info", "leave"]
    slowPrint("Welcome to town!")
    userInput = ""
    while userInput not in options:
        slowPrint(f"Options: {options}")
        userInput = input()
        if userInput == "inn":
            inn(player)
        elif userInput == "blacksmith":
            blacksmith(player)
        elif userInput == "armoury":
            armoury(player)
        elif userInput == "shop":
            shop(player)
        elif userInput == "info":
            player.info()
        elif userInput == "leave":
            crossroadsScene(player)
        else:
            slowPrint("Please enter a valid option.")
        userInput = ""

def puzzleRoom(player):
    slowPrint("The puzzle is not ready yet!")
    crossroadsScene(player)

"""
                                        ????????
                                           ^
                                           |
                                      hauntedRoom (Needs Key)
                                           ^
                                           |
shadowFight <-- showShadowFigure <-- crossroadsScene --> showSkeletons --> toTown --> inn/blacksmith/armoury/shop
                                           ^
                                           |
                                       introScene
"""

