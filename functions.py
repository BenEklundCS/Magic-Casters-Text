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
def slow_print(text):
  # take text and print it character by character
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Quick method to end the game
def game_over():
    slow_print("You have lost! The kingdom is doomed!")
    slow_print("GAME OVER")
    input()
    exit()

# Fight loop
def fight(player, monster, playerTurn):
    options = ["slash", "slam", "info", "pass"]
    user_input = ""
    # If monsters turn, attack the player
    if playerTurn == False:
        monster.chooseAttack(player)
    # If the player is dead, call gameOver
    if player.checkDeath() == True:
        game_over()
    while user_input not in options:
        slow_print("It is your turn to attack.")
        slow_print(f"Options: {options}")
        user_input = input()
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
            game_over()
        # Reset for next iteration
        user_input = ""

    return False

def print_attack(self, monster, roll):
    raw_damage = roll + self.getAttack()
    total_damage = raw_damage - monster.getDefense()
    slow_print("You rolled a {} for your slam attack for {} damage.".format(roll, raw_damage))
    slow_print("{} absorbed {} damage, for {} total damage.".format(monster.getName(), monster.getDefense(), total_damage))
    monster.setHealth(monster.getHealth() - total_damage)
    slow_print("The {}'s health is now {}".format(monster.getName(), monster.getHealth()))
