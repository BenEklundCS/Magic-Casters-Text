from functions import slow_print, d4, d6


class Monster:

    def __init__(self, name, health, mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.gold = gold

    def check_death(self, player):
        if self.health <= 0:
            slow_print("You have won the battle! The {} had {} gold on its body.".format(self.name, self.gold))
            player.gold = player.gold + self.gold
            slow_print("You now have {} gold!".format(player.gold))
            return True
        else:
            return False
        # Basic monster attack, rolls a d4 and adds the attack of the monster to it, then subtracts the player's defense.
    def normal_attack(self, player):
        slow_print("The {} attacks you!".format(self.name)) # "The monster attacks you"
        roll = d4()
        damage = roll + self.attack - player.defense
        slow_print("{} rolled a {} for {} total damage.".format(self.name, roll, damage)) # "Monster rolled a 6 for 15 total damage."
        player.health = player.health - damage
        slow_print("Your health is now {}/{}.".format(player.health, player.max_health)) # "Your health is now 50/100."

    # Selects an attack, placeholder that only has one option and a miss for now
    def choose_attack(self, player):
        roll = d6()
        if roll != 1:
            self.normal_attack(player) 
        else:
            slow_print("The {} missed!".format(self.name)) # "The monster missed!"
      
# Goblin class inherits from monster class
class Goblin(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Goblin", 20, 0, 5, 0, 10)

# shadowFigure class inherits from monster class
class shadowFigure(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Shadowy Figure", 40, 0, 8, 5, 50)

