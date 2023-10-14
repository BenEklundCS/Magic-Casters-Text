""" Module imports """
from player import Player
from monsters import ShadowFigure, Goblin
from functions import slow_print, fight
from puzzles import memory_puzzle

# Initial scene function | introScene() --> crossroadsScene(player)
# player object is generated in introScene() with a user made name

def intro_scene():
    """ Starting scene for CH1 """
    slow_print("Welcome to Magic Casters Text!")
    slow_print("Please enter your name: ")
    name = input()
    # name, health, maxHealth, mana, maxMana, attack, defense, gold
    player = Player(name, 30, 30, 50, 50, 8, 0, 100)
    slow_print(f"Hi {player.name}, it is a pleasure to meet you!")
    slow_print("I am that handy voice in your head - here to guide you on your journey!")
    slow_print("These lands are perilous, and there is no coming back from death.")
    slow_print("Proceed with caution, friend.")
    crossroads_scene(player)

# crossroadsScene is the hub of chapter 1
# Boolean flags in function header to control which paths are taken

def crossroads_scene(player):
    directions = ["left", "right", "forward", "backward"]
    slow_print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    user_input = ""
    while user_input not in directions:
        slow_print(f"Options: {directions}")
        user_input = input()

        # Left
        if user_input == "left" and player.progress["CH1"]["crossroads_scene"]["left_completed"] is False:
            show_shadow_figure(player)
        elif user_input == "left" and player.progress["CH1"]["crossroads_scene"]["left_completed"] is True:
            slow_print(
                "You've already gone this way, and there's nothing left to find.")
            user_input = ""

        # Right
        elif user_input == "right" and player.progress["CH1"]["crossroads_scene"]["right_completed"] is False:
            goblin_fight(player)  # Not yet defined
        elif user_input == "right" and player.progress["CH1"]["crossroads_scene"]["right_completed"] is True:
            to_town(player)

        # Forward
        elif user_input == "forward":
            puzzle_room(player)  # Not yet defined

        # Backward
        elif user_input == "backward":
            slow_print(
                "You find that this door opens into a wall. Maybe another direction would be better?")
            user_input = ""
        else:
            slow_print("Please enter a valid option.")

# Intro to shadowFigure fight | showShadowFigure(player) --> shadowFight(player)

def show_shadow_figure(player):
    """ Show shadowy figure """
    options = ["run", "fight"]
    slow_print("You see a shadowy figure in the distance. It is approaching you.")
    slow_print("What do you do?")
    user_input = ""
    while user_input not in options:
        slow_print(f"Options: {options}")
        user_input = input()
        if user_input == "run":
            slow_print("You run away from the shadowy figure.")
            slow_print("You find yourself back at the crossroads.")
            crossroads_scene(player)
        elif user_input == "fight":
            slow_print("You fight the shadowy figure.")
            shadow_fight(player)
        else:
            slow_print("Please enter a valid option.")
            user_input = ""

def shadow_fight(player):
    """ Shadow fight on left path """
    # name, health, mana, attack, defense, gold
    monster = ShadowFigure("Shadowy Figure", 50, 100, 15, 0, 50)
    if fight(player, monster, True) is True:
        slow_print(
            "You also find a key on the shadowy figure's body. Maybe it will be useful later?"
        )
        player.progress["CH1"]["crossroads_scene"]["left_completed"] = True
        crossroads_scene(player)
    return True

def goblin_fight(player):
    """ Goblin fight on right path """
    monster = Goblin("Gob", 25, 50, 10, 0, 100)
    slow_print("A goblin has appeared!")
    if fight(player, monster, True) is True:
        player.progress["CH1"]["crossroads_scene"]["right_completed"] = True
        slow_print(
            "You see the light of a town up ahead, and decide to continue down the trail towards it.")
        to_town(player)
    return True

def to_town(player):
    """ Head to town hub """
    options = ["inn", "blacksmith", "armoury", "shop", "info", "leave"]
    slow_print("Welcome to town!")
    user_input = ""
    while user_input not in options:
        slow_print(f"Options: {options}")
        user_input = input()
        if user_input == "inn":
            inn(player)
        elif user_input == "blacksmith":
            blacksmith(player)
        elif user_input == "armoury":
            armoury(player)
        elif user_input == "shop":
            shop(player)
        elif user_input == "info":
            player.info()
        elif user_input == "leave":
            crossroads_scene(player)
        else:
            slow_print("Please enter a valid option.")
        user_input = ""

def inn(player):
    """ Town inn """
    slow_print(f"Dave (Innkeeper): Hi {player.name}, welcome to our humble inn!\n Here you can spend some coin to stay the night and rest up.")


def blacksmith(player):
    """ Town blacksmith """
    slow_print(f"Quinn (Blacksmith): Welcome to my blacksmithing shop {player.name}!\n I'm willing to upgrade your attacks if you have gold to spare")


def armoury(player):
    """ Town armoury """
    slow_print(f"Shelly (Armourer): Welcome to my armoury {player.name}!\n Your armor could use a tune up if you've got the gold to spare.")


def shop(player):
    """ Town shop """
    slow_print(f"Mary (Shopkeep): Welcome to my shop {player.name}!\n You can buy stuff here.")


def puzzle_room(player):
    """ Puzzle on up path """
    if memory_puzzle() is True:
        print("You've completed the puzzle!")
    crossroads_scene(player)
