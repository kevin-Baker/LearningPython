import os
import re
import glob
dirLength = 0
counter = 0
regex = "def\s+[_A-Za-z0-9]+\s*\(.*\)\s*\:"
for file in glob.glob("*.py"):
    print(file)
    with open(file, 'r') as myfile: #reads the contents of each file
        data = myfile.read()
        #print(data)
        test_str = data # REGEX proccsor that finds all function names
        matches = re.finditer(regex, test_str, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
        
            print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
            
                print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                