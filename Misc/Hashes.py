#import sys
def fnv_hash(string, seed=0):
    #Constants
    FNV_prime = 16777619
    offset_basis = 2166136261
    hash = offset_basis + seed  #FNV-1a Hash algorithm
    for char in string:
        hash = hash * FNV_prime
        hash = hash ^ ord(char)
        #https://portal0013.globalview.adp.com/gvfrmwk3/HPI.home#/areadashboard
    return hash

class StringHasher:
    stringHashes = {}S
    def readTextFile(self,fileName):
        file_ = open(fileName,"r")
        fileContent = file_.read()
        file_.close()
        lines = fileContent.split("\n")
        limit = len(lines)
        for element in lines :
            # self.element is each individual line
            self.stringHashes[fnv_hash(element)] = element

    def LookupString(self,hash): #Here
        stringFromHash = ""
        stringFromHash = self.stringHashes[hash]
        print(stringFromHash)

    def printHashedStrings(self):
        for key in self.stringHashes :
            print(key, "",self.stringHashes[key])
        
textIn = "hash.txt"
myStringHasher = StringHasher()
myStringHasher.readTextFile(textIn)
myStringHasher.LookupString(2879634789696116011719252020689678733822719984) #Here
myStringHasher.printHashedStrings() 