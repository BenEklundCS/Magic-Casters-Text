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
        slowPrint("You slash the {}.".format(monster.getName()))
        roll = d6()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a {} for your slash attack for {} damage.".format(roll, damage))
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The {}'s health is now {}".format(monster.getName(), monster.getHealth()))
        
    def slam(self, monster):
        self.setMana(self.getMana() - 5)
        slowPrint("You slam the {} {}/{} mana left.".format(monster.getName(), self.getMana(), self.getMaxMana()))
        roll = d8()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a {} for your slam attack for {} damage.".format(roll, damage))
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The {}'s health is now {}".format(monster.getName(), monster.getHealth()))
        
    def passTurn(self):
        slowPrint("You pass your turn.")

    def info(self):
        slowPrint("Name: {}".format(self.getName()))
        slowPrint("Health: {}".format(self.getHealth()))
        slowPrint("Max Health: {}".format(self.getMaxHealth()))
        slowPrint("Mana: {}".format(self.getMana()))
        slowPrint("Max Mana: {}".format(self.getMana()))
        slowPrint("Attack: {}".format(self.getAttack()))
        slowPrint("     Slash: 1d6 + base | Costs 0 mana")
        slowPrint("     Slam: 1d8 + base | Costs 5 mana")
        slowPrint("Defense: {}".format(self.getDefense()))
        slowPrint("Gold: {}".format(self.getGold()))
        

  
    
    