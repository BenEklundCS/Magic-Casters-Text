from player import Player
from monsters import Monster, shadowFigure
from functions import slowPrint, fight

# Initial scene function | introScene() --> crossroadsScene(player)
# player object is generated in introScene() with a user made name
def introScene():
    slowPrint("Welcome to Magic Casters Text!")
    slowPrint("Please enter your name: ")
    name = input()
    player = Player(name, 100, 100, 50, 50, 30, 0, 100)  # name, health, maxHealth, mana, maxMana, attack, defense
    slowPrint("Hi {}, it is a pleasure to meet you!".format(player.getName()))
    slowPrint("I am that handy voice in your head - here to guide you on your journey!")
    slowPrint("These lands are perilous, and there is no coming back from death.")
    slowPrint("Proceed with caution, friend.")
    crossroadsScene(player)

# crossroadsScene is the hub of chapter 1
# Boolean flags in function header to control which paths are taken

def crossroadsScene(player, leftCompleted=False, rightCompleted=False, forwardCompleted=False):
    directions = ["left", "right", "forward"]
    slowPrint("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        slowPrint(f"Options: {directions}")
        userInput = input()
        # Left
        if userInput == "left" and leftCompleted == False:
            showShadowFigure(player)
        elif userInput == "left" and leftCompleted == True:
            slowPrint("You've already gone this way, and there's nothing left to find.")
            crossroadsScene(player, True)
        # Right
        elif userInput == "right":
            showSkeletons()  # Not yet defined
        # Forward
        elif userInput == "forward":
            hauntedRoom()  # Not yet defined
        # Backward
        elif userInput == "backward":
            slowPrint("You find that this door opens into a wall. Maybe another direction would be better?")
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
            slowPrint("Please enter a valid option for the adventure game.")

# Shadow fight troubleshooting
def shadowFight(player):
    monster = shadowFigure("Shadowy Figure", 50, 100, 15, 0, 50) # name, health, mana, attack, defense, gold
    if fight(player, monster, True) == True:
        del monster
        slowPrint(
            "You also find a key on the shadowy figure's body. Maybe it will be useful later?"
        )
        crossroadsScene(player, True, False, False)
    return True
# Under dev
def showSkeletons():
    toTown()
# Town 
def toTown():
    options = []
    slowPrint("Welcome to town!")
    userInput = ""
    while userInput not in options:
        slowPrint(f"Options: {options}")
"""
                                        ????????
                                           ^
                                           |
                                      hauntedRoom (Needs Key)
                                           ^
                                           |
shadowFight <-- showShadowFigure <-- crossroadsScene --> showSkeletons --> toTown
                                           ^
                                           |
                                       introScene
"""

