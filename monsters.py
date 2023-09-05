from functions import slow_print, d4, d6


class Monster:

    def __init__(self, name, health, mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.gold = gold

    # Setters
    def setName(self, name):
        self.name = name

    def setHealth(self, health):
        self.health = health

    def setMana(self, mana):
        self.mana = mana

    def setAttack(self, attack):
        self.attack = attack

    def setDefense(self, defense):
        self.defense = defense

    def setGold(self, gold):
        self.gold = gold

    # Getters
    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getMana(self):
        return self.mana

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getGold(self):
        return self.gold

    def checkDeath(self, player):
        if self.getHealth() <= 0:
            slow_print("You have won the battle! The {} had {} gold on its body.".format(self.getName(), self.getGold()))
            player.setGold(player.getGold() + self.getGold())
            slow_print("You now have {} gold!".format(player.getGold()))
            return True
        else:
            return False
        # Basic monster attack, rolls a d4 and adds the attack of the monster to it, then subtracts the player's defense.
    def normalAttack(self, player):
        slow_print("The {} attacks you!".format(self.getName())) # "The monster attacks you"
        roll = d4()
        damage = roll + self.getAttack() - player.getDefense()
        slow_print("{} rolled a {} for {} total damage.".format(self.getName(), roll, damage)) # "Monster rolled a 6 for 15 total damage."
        player.setHealth(player.getHealth() - damage)
        slow_print("Your health is now {}/{}.".format(player.getHealth(), player.getMaxHealth())) # "Your health is now 50/100."

    # Selects an attack, placeholder that only has one option and a miss for now
    def chooseAttack(self, player):
        roll = d6()
        if roll != 1:
            self.normalAttack(player) 
        else:
            slow_print("The {} missed!".format(self.getName())) # "The monster missed!"
      
# Goblin class inherits from monster class
class Goblin(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Goblin", 20, 0, 5, 0, 10)

# shadowFigure class inherits from monster class
class shadowFigure(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__("Shadowy Figure", 40, 0, 8, 5, 50)

