#read in big json file.
#Seperate the teams into different Json files by team name ('49ers.json' ...)
import json
destination = "C:\\Users\\bakerke\\Documents\\Projects\\NFL2020\\"

with open("allTeams-11-16-2019.js", "r") as read_file:
    data = json.load(read_file)
    for element in data["allTeams2020"]:
        print(element['team'])
        new_file = open(destination + element['team']+'.json', "w+")
        json.dump(element,new_file,indent=2)
        new_file.close()

        
       
            
