import time
import sys
from scenes import *
from player import *
from monsters import *


def main():
    player = Player("Ben", 100, 100, 50, 50, 30, 0, 100)  # name, health, maxHealth, mana, maxMana, attack, defense
    shadowFight(player)
main()