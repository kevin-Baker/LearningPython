class Person:
    arms = 2 
    legs = 2 
    phoneBook = {} 
    
    def read(self,book):
        print("I am reading %s"  % (book))
    def addFreindNumber(self,name,number):
        self.phoneBook[name] = number 
        print(self.phoneBook)
        

    def lookupFreindPhoneNumber(self,name):
        if name in self.phoneBook:
            return self.phoneBook[name]
        else:
            return None
        



newbook = "War and Peace"
bob = Person()
bob.read(newbook)
bob.addFreindNumber("Jenny", "8675309")
print(bob.lookupFreindPhoneNumber("Jenny"))
print(bob.lookupFreindPhoneNumber("Travis"))