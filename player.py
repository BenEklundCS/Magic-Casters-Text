# Player class for MagicCasters
from functions import slowPrint, d8, d6
from monsters import Monster

class Player:
    def __init__(self, name, health, maxHealth, mana, maxMana, attack, defense, gold):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.mana = mana
        self.maxMana = maxMana
        self.attack = attack
        self.defense = defense
        self.gold = gold
        
    # Setters
    def setName(self, name):
        self.name = name
    def setHealth(self, health):
        if health >= self.getMaxHealth():
          self.health = self.getMaxHealth()
        self.health = health
    def setMaxHealth(self, maxHealth):
        self.maxHealth = maxHealth
    def setMana(self, mana):
        if mana >= self.getMaxMana():
          self.mana = self.getMaxMana()
        self.mana = mana
    def setMaxMana(self, maxMana):
        self.maxMana = maxMana
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
    def getMaxHealth(self):
        return self.maxHealth
    def getMana(self):
        return self.mana
    def getMaxMana(self):
        return self.maxMana
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getGold(self):
        return self.gold
      
    # Functions
    def checkDeath(self):
      if self.getHealth() <= 0:
        slowPrint("You have died.")
        return True
      else:
        return False
    # Attacks
  
    def slash(self, monster):
        slowPrint("You slash the " + monster.getName() + ".")
        roll = d6()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a " + str(roll) + " for your slash attack for " + str(damage) + " damage.")
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The " + str(monster.getName()) + "'s health is now " + str(monster.getHealth()))
        
    def slam(self, monster):
        self.setMana(self.getMana() - 5)
        slowPrint("You slam the " + monster.getName() + " " + str(self.getMana()) + "/50 mana left.")
        roll = d8()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a " + str(roll) + " for your slam attack for " + str(damage) + " damage.")
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The " + str(monster.getName()) + "'s health is now " + str(monster.getHealth()))
        
    def passTurn(self):
        slowPrint("You pass your turn.")
    def info(self):
        print("Name: {}".format(self.getName()))
        print("Health: {}".format(self.getHealth()))
        print("Max Health: {}".format(self.getMaxHealth()))
        print("Mana: {}".format(self.getMana()))
        print("Max Mana: {}".format(self.getMana()))
        print("Attack: {}".format(self.getAttack()))
        print("     Slash: 1d6 + base | Costs 0 mana")
        print("     Slam: 1d8 + base | Costs 5 mana")
        print("Defense: {}".format(self.getDefense()))
        print("Gold: {}".format(self.getGold()))
        

  
    
    