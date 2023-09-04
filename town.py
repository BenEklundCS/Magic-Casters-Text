from functions import slowPrint
from player import *

def inn(player):
    slowPrint("Dave (Innkeeper): Hi {}, welcome to our humble inn!\n Here you can spend some coin to stay the night and rest up.".format(player.getName()))
def blacksmith(player):
    slowPrint("Quinn (Blacksmith): Welcome to my blacksmithing shop {}!\n I'm willing to upgrade your attacks if you have gold to spare".format(player.getName()))
def armoury(player):
    slowPrint("Shelly (Armourer): Welcome to my armoury {}!\n Your armor could use a tune up if you've got the gold to spare.".format(player.getName()))
def shop(player):
    slowPrint("Mary (Shopkeep): Welcome to my shop {}!\n You can buy stuff here.".format(player.getName()))