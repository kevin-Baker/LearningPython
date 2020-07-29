import os.path
from os import path
import json
import os
import sys
"""
t = lookupTeam(teamName)
p =  lookupPlayer(team, fname, lname)
printAttribute(p, attribute)
p = modifyAttribute(p, attribute, newValue)
"""
#entries = os.scandir('C:\\Users\\bakerke\\Documents\\Projects\\NFL2020\\')
def lookupTeam(teamname):
    filename = 'C:\\Users\\bakerke\\Documents\\Projects\\NFL2020\\' + teamname + '.json'
    team = None
    if path.exists(filename):
        with open(filename, "r") as read_file: # open file and extract data
            team = json.load(read_file) 
    return team
def lookupPlayer(team, fname, lname):
    players = team['docs']
    retVal = None 
    for player in players: 
        if fname == player['firstName'] and lname == player['lastName']:
            retVal = player
            break
    return retVal 

def modifyAttribute(player, attribute, newValue):
    if attribute in player.keys():
        print("Orignal " + attribute + " = " + player[attribute])
        player[attribute] = newValue
        return True
    else:
        return False
    
def saveTeam(team):
    filename = 'C:\\Users\\bakerke\\Documents\\Projects\\NFL2020\\' + team['team'] + '.json'
    new_file = open(filename,"w+")
    json.dump(team,new_file,indent=2)

def printPlayerAttribute(player,attribute):
    print( attribute + " = " + player[attribute])

def help():
    print("How to modify: Enter the last name first, then the first name, then the team name, then the attribute and then the new value")
    print("ex: Miller Von Broncos awareness_rating 99")
    print("How to print: Enter the last name first, then the first name, then the team name, then the attribute")
    print("ex: Ramsey Jalen Rams awareness_rating")

# 1 = team 2 = fname 3 = lname 4 = attribute 5 = new value 
# 1 = fname 2 = lname 3 = team 4 = att 5 = new val 
# 1 = attribute 2 = new value 3 = team 4 = fname 5 = lname
# 1 = lname 2 = fname 3 = team 4 = att 5 = new val //This One//

if (len(sys.argv) < 5):
    help()
else: 
    team = lookupTeam(sys.argv[3])
    if (team == None):
        print("Invaild team name")
        exit(1)
    player = lookupPlayer(team, sys.argv[2], sys.argv[1])
    if (player == None):
        print("Player not found")
        exit(1)
    if (len(sys.argv) == 6):
        boolean = modifyAttribute(player,sys.argv[4], sys.argv[5])
        if(boolean == False):
            print("Invalid attribute " + sys.argv[4])
            exit(1)
        saveTeam(team)
    printPlayerAttribute(player,sys.argv[4])
    

#Lookup the player anvvv 
"""
ModifyPlayer.py  args: <fName> <lname> <team> <attribute> <newValue>  

Given a player's name, team, attribute and new value (command line args) :
	Lookup the player and change the attribute to the new given value, save the file 
	Lookup the player and print the given attribute
    """