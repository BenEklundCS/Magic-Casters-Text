from functions import slowPrint, d4, d6


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
            slowPrint("You have won the battle! The {} had {} gold on its body.".format(self.getName(), self.getGold()))
            player.setGold(player.getGold() + self.getGold())
            slowPrint("You now have {} gold!".format(player.getGold()))
            return True
        else:
            return False
      
# Goblin class inherits from monster class
class Goblin(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__(name, health, mana, attack, defense, gold)
        self.name = "Goblin"
        self.health = 50
        self.mana = 0
        self.attack = 10
        self.defense = 5
        self.gold = 10
    
class shadowFigure(Monster):
    def __init__(self, name, health, mana, attack, defense, gold):
        super().__init__(name, health, mana, attack, defense, gold)
        self.name = "Shadowy Figure"
        self.health = 100
        self.mana = 0
        self.attack = 15
        self.defense = 5
        self.gold = 50
    
    # Basic monster attack, rolls a d4 and adds the attack of the monster to it, then subtracts the player's defense.
    def normalAttack(self, player):
        slowPrint("The " + self.getName() + " attacks you!")
        roll = d4()
        damage = roll + self.getAttack() - player.getDefense()
        slowPrint(str(self.getName()) + " rolled a " + str(roll) + " for " + str(damage) +" total damage.")
        player.setHealth(player.getHealth() - damage)
        slowPrint("Your health is now " + str(player.getHealth()) + "/" + str(player.getMaxHealth()) + ".")

    def chooseAttack(self, player):
        roll = d6()
        if roll != 1:
            self.normalAttack(player)
        else:
            slowPrint("The " + self.getName() + " missed!")
