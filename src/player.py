""" Functions used for player class """
from functions import slow_print, roll_d8, roll_d6, print_attack, color

class Player:
    """ Player class definition """
    def __init__(self, name, health, max_health, mana, max_mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.progress = { # Solution to global tracking of progress for now
                        "CH1":
                            {
                            "crossroads_scene":
                                {
                                "left_completed":False, # Shadow Figure
                                "right_completed":False, # Goblin Encounter
                                "forward_completed":False # puzzle
                                }
                            }
                        }

    # Functions
    
    def check_death(self):
        """ Checks if the player is dead """
        if self.health <= 0:
            slow_print(color("You have died.", "red"))
            return True
        return False

    # Player actions

    def slash(self, monster):
        """ Slash attack for 1d6 """
        slow_print(f"You slash the {monster.name}.")
        roll = roll_d6()
        print_attack(self, monster, roll, "slash")

    def slam(self, monster):
        """ Slam attack for 2d8 and costs 5 mana """
        self.mana = self.mana - 5
        slow_print(f"You slam the {monster.name}, -5 mana, {self.mana}/{self.max_mana} mana left")
        roll = roll_d8()+roll_d8()
        print_attack(self, monster, roll, "slam")

    # Utility

    def pass_turn(self):
        """ Pass turn (do nothing) """
        slow_print("You pass your turn.")

    def info(self):
        """ Prints all player class info """
        slow_print(f"Name: {self.name}")
        slow_print(f"Health: {self.health}/{self.max_health}")
        slow_print(f"Mana: {self.mana}/{self.max_mana}")
        slow_print(f"Attack: {self.attack}")
        slow_print("     Slash: 1d6 + base | Costs 0 mana")
        slow_print("     Slam: 1d8 + base | Costs 5 mana")
        slow_print(f"Defense: {self.defense}")
        slow_print(f"Gold: {self.gold}")

    def rest(self):
        """ Full heal player """
        self.health = self.max_health
        slow_print(f"You awaken feeling well rested! (HP: {self.health}/{self.max_health})")

    def charge(self, gold):
        """ Player pays gold """
        self.gold = self.gold - gold
        slow_print(f"You pay {gold} gold ({self.gold} gold remaining)")

def initialize_player():
    """ Initialize the player """
    slow_print("\nPlease enter your name: ")
    name = input()
    # name, health, maxHealth, mana, maxMana, attack, defense, gold
    player = Player(name, 50, 30, 50, 50, 10, 0, 100) # Initialize player
    slow_print(f"Welcome to the lands of Magic Casters {player.name}!\n")
    return player
