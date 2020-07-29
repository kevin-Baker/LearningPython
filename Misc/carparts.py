import sys 
import os.path
from os import path
def printHelp() :
    print("Usage : carparts.py partnumber cars.txt")
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv) > 1 :
    if not path.exists(sys.argv[1]):
        print("error file does not exist")
        exit(1)   
    file_parts=open(sys.argv[1],"r")
    fileInfo = file_parts.read()
    lineSplit = fileInfo.split("\n")
    print("length of file" , len(lineSplit))
    print(fileInfo)
    searchTerm = sys.argv[2]
    #searchTerm = input("Enter the part number")
    file_parts.close()
    i = 0
    element = ""
    limit = len(lineSplit)
    while(i < limit):
        element = lineSplit[i]
        if(element.find(searchTerm) > -1):
            # Index??? I found it yesterday while searching
            print("The part number was found on line " , i , ": ", element )
        i += 1 
        

        


'''
# loops
while (condition): # i < 10 
    # stuff to execute 

for element in array : 
    # stuff to execute 
'''
    
        
        
        
        
        
        
        
        
        
         
