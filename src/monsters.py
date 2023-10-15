""" Functions module """
from functions import slow_print, roll_d4, roll_d6

class Monster:
    """ Monster class """

    def __init__(self, name, health, mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.gold = gold

    def check_death(self, player):
        """ Check if monster is dead and add gold to player """

        if self.health <= 0:
            slow_print(f"You have won the battle! The {self.name} had {self.gold} gold on its body.")
            player.gold = player.gold + self.gold
            slow_print(f"You now have {player.gold} gold!")
            return True
        return False

    def normal_attack(self, player):
        """ Basic monster attack, rolls a d4 and adds the attack of the monster to it, then subtracts the player's defense. """

        slow_print(f"The {self.name} attacks you!") # "The monster attacks you"
        roll = roll_d4()
        damage = roll + self.attack - player.defense
        slow_print(f"{self.name} rolled a {roll} for {damage}")
        player.health = player.health - damage
        slow_print(f"Your health is now {player.health}/{player.max_health}.")

    # Selects an attack, placeholder that only has one option and a miss for now
    def choose_attack(self, player):
        """ Choose a random attack, or miss """

        roll = roll_d6()
        if roll != 1:
            self.normal_attack(player) 
        else:
            slow_print(f"The {self.name} missed!")
      
# Goblin class inherits from monster class
class Goblin(Monster):
    """ Goblin """

    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Goblin", 20, 0, 5, 0, 10)

# shadowFigure class inherits from monster class
class ShadowFigure(Monster):
    """ Shadowy Figure """
    
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Shadowy Figure", 40, 0, 8, 5, 50)

