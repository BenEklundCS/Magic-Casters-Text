# Player class for MagicCasters
from functions import slow_print, d8, d6, print_attack
from monsters import Monster

class Player:
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
      if self.health <= 0:
        slow_print("You have died.")
        return True
      else:
        return False

    # Player actions

    # Attacks
    # Slash attack, no mana but only 1d6 + base

    def slash(self, monster):
        slow_print("You slash the {}.".format(monster.name))
        roll = d6()
        print_attack(self, monster, roll)
        
    # Slam attack, costs mana for 2d8 + base
    def slam(self, monster):
        self.mana = self.mana - 5
        slow_print("You slam the {} {}/{} mana left.".format(monster.name, self.mana, self.max_mana))
        roll = d8()+d8()
        print_attack(self, monster, roll)

    # Utility
    # Function to skip turn if needed
    def pass_turn(self):
        slow_print("You pass your turn.")
        
    # Info will be called from any player input to print all current stats
    def info(self):
        slow_print("Name: {}".format(self.name))
        slow_print("Health: {}/{}".format(self.health, self.max_health))
        slow_print("Mana: {}/{}".format(self.mana, self.max_mana))
        slow_print("Attack: {}".format(self.attack))
        slow_print("     Slash: 1d6 + base | Costs 0 mana")
        slow_print("     Slam: 1d8 + base | Costs 5 mana")
        slow_print("Defense: {}".format(self.defense))
        slow_print("Gold: {}".format(self.gold))
     
        

  
    
    