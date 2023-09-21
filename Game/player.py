""" Functions used for player class """
from functions import slow_print, d8, d6, print_attack

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
        #self.actions = {"slash":True, "slam":True, "info":True, "pass":True} unlockable actions over time by building "options" from the key and values of this variable
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
            slow_print("You have died.")
            return True
        return False

    # Player actions

    def slash(self, monster):
        """ Slash attack for 1d6 """
        slow_print(f"You slash the {monster.name}.")
        roll = d6()
        print_attack(self, monster, roll)
        
    # Slam attack, costs mana for 2d8 + base
    def slam(self, monster):
        """ Slam attack for 2d8 and costs 5 mana """
        self.mana = self.mana - 5
        slow_print(f"You slam the {monster.name} {self.mana}/{self.max_mana}")
        roll = d8()+d8()
        print_attack(self, monster, roll)

    # Utility
    # Function to skip turn if needed
    def pass_turn(self):
        """ Pass turn (do nothing) """
        slow_print("You pass your turn.")
        
    # Info will be called from any player input to print all current stats
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