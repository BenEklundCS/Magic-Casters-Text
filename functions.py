import time
import random
import sys

# Dice
def d2():
    return random.randint(1, 2)

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
    # If monsters turn, attack the player
    if playerTurn == False:
        monster.chooseAttack(player)
    # If the player is dead, call gameOver
    if player.checkDeath() == True:
        gameOver()
    while userInput not in options:
        slowPrint("It is your turn to attack.")
        slowPrint(f"Options: {options}")
        userInput = input()
        # Possible user attacks
        if userInput == "slash":
            player.slash(monster)
        elif userInput == "slam":
            player.slam(monster)
        # User utility options
        elif userInput == "info":
            player.info()
            userInput = ""
            continue
        elif userInput == "pass":
            player.passTurn()
        # Error handling
        else:
            slowPrint("Invalid option. Please enter a valid attack!")
            continue
        # Did player action kill the monster?
        if monster.checkDeath(player) == True:
            return True
        # Attack the player
        monster.chooseAttack(player)
        # Did the player die?
        if player.checkDeath() == True:
            gameOver()
        # Reset for next iteration
        userInput = ""

    return False

def printAttack(self, monster, roll):
    rawDamage = roll + self.getAttack()
    totalDamage = rawDamage - monster.getDefense()
    slowPrint("You rolled a {} for your slam attack for {} damage.".format(roll, rawDamage))
    slowPrint("{} absorbed {} damage, for {} total damage.".format(monster.getName(), monster.getDefense(), totalDamage))
    monster.setHealth(monster.getHealth() - totalDamage)
    slowPrint("The {}'s health is now {}".format(monster.getName(), monster.getHealth()))
