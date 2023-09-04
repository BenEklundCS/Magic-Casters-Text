import time
import random
import sys


# Dice
def d4():
    return random.randint(1, 4)

def d6():
    return random.randint(1, 6)

def d8():
     return random.randint(1, 8)

def d20():
     return random.randint(1, 20)

# Other stuff
def slowPrint(text):
  # take text and print it character by character
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Quick method to end the game
def gameOver():
    slowPrint("You have lost! The kingdom is doomed!")
    slowPrint("GAME OVER")
    input()
    exit()

# Fight loop
def fight(player, monster, playerTurn):
    options = ["slash", "slam", "info", "pass"]
    userInput = ""
    if playerTurn == False:
        monster.chooseAttack(player)
    if player.checkDeath() == True:
        gameOver()
    while userInput not in options:
        slowPrint("It is your turn to attack.")
        slowPrint(f"Options: {options}")
        userInput = input()
        if userInput == "slash":
            player.slash(monster)
        elif userInput == "slam":
            player.slam(monster)
        elif userInput == "info":
            player.info()
            continue
        elif userInput == "pass":
            player.passTurn()
        else:
            slowPrint("Invalid option. Please enter a valid attack!")
            continue
        if monster.checkDeath(player) == True:
            return True
        monster.chooseAttack(player)
        if player.checkDeath() == True:
            gameOver()
        userInput = ""

    return False
