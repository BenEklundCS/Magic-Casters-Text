# Player class for MagicCasters
from functions import slow_print, d8, d6, print_attack
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
        #self.actions = {"slash":True, "slam":True, "info":True, "pass":True} unlockable actions over time by building "options" from the key and values of this variable
        self.progress = { # Solution to global tracking of progress for now
                        "CH1":
                            {
                            "crossroadsScene":
                                {
                                "leftCompleted":False, # Shadow Figure
                                "rightCompleted":False, # Goblin Encounter
                                "forwardCompleted":False # puzzle
                                }
                            }
                        }
        
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
        slow_print("You have died.")
        return True
      else:
        return False

    # Player actions

    # Attacks
    # Slash attack, no mana but only 1d6 + base

    def slash(self, monster):
        slow_print("You slash the {}.".format(monster.getName()))
        roll = d6()
        print_attack(self, monster, roll)
        
    # Slam attack, costs mana for 2d8 + base
    def slam(self, monster):
        self.setMana(self.getMana() - 5)
        slow_print("You slam the {} {}/{} mana left.".format(monster.getName(), self.getMana(), self.getMaxMana()))
        roll = d8()+d8()
        print_attack(self, monster, roll)

    # Utility
    # Function to skip turn if needed
    def passTurn(self):
        slow_print("You pass your turn.")
        
    # Info will be called from any player input to print all current stats
    def info(self):
        slow_print("Name: {}".format(self.getName()))
        slow_print("Health: {}/{}".format(self.getHealth(), self.getMaxHealth()))
        slow_print("Mana: {}/{}".format(self.getMana(), self.getMaxMana()))
        slow_print("Attack: {}".format(self.getAttack()))
        slow_print("     Slash: 1d6 + base | Costs 0 mana")
        slow_print("     Slam: 1d8 + base | Costs 5 mana")
        slow_print("Defense: {}".format(self.getDefense()))
        slow_print("Gold: {}".format(self.getGold()))
     
        

  
    
    