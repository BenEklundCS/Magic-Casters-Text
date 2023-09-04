from player import Player
from monsters import Monster, shadowFigure
from functions import slowPrint, fight

# Verified and working
def introScene():
    slowPrint("Welcome to Magic Casters Text!")
    slowPrint("Please enter your name: ")
    name = input()
    player = Player(name, 100, 100, 50, 50, 30, 0, 100)  # name, health, maxHealth, mana, maxMana, attack, defense
    slowPrint("Hi " + str(player.getName()) + ", it is a pleasure to meet you!")
    slowPrint("I am that handy voice in your head - here to guide you on your journey!")
    slowPrint("These lands are perilous, and there is no coming back from death.")
    slowPrint("Proceed with caution, friend.")
    crossroadsScene(player)
# Left path is under development
def crossroadsScene(player, leftCompleted=False, rightCompleted=False, forwardCompleted=False):
    directions = ["left", "right", "forward"]
    slowPrint("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        slowPrint("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left" and leftCompleted == False:
            showShadowFigure(player)
        elif userInput == "left" and leftCompleted == True:
            slowPrint("You've already gone this way, and there's nothing left to find.")
            crossroadsScene(player, True)
        elif userInput == "right":
            showSkeletons()  # Not yet defined
        elif userInput == "forward":
            hauntedRoom()  # Not yet defined
        elif userInput == "backward":
            slowPrint("You find that this door opens into a wall. Maybe another direction would be better?")
        else:
                slowPrint("Please enter a valid option.")
# This works fine
def showShadowFigure(player):
    slowPrint("You see a shadowy figure in the distance. It is approaching you.")
    slowPrint("What do you do?")
    userInput = ""
    while userInput not in ["run", "fight"]:
        slowPrint("Options: run/fight")
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



