import sys 
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

# need to check if we have enough arguments 
# Write a python program that takes your command line argument
# and does a parts search --> through a text file ; print out the matching lines 
# show the results on the terminal / console 
if len(sys.argv) > 1 :
    file_op = open(sys.argv[1],"r")
    fileContent = file_op.read()
    file_op.close() 

    usevar = "Kevin"
    print (fileContent)
    print (fileContent.find(usevar) )

    if fileContent.find(usevar) > -1 :
        print("Yes") 

'''
print(file_op.read())
usevar = "Kevin"
linvar = 5
call = 0
countercall =  1
while (call != countercall):
    if usevar == (file_op.readline(linvar)):
        print("Username found")
        
        countercall = 0
    else:
        print("name not found")
        linvar = linvar + 5

file_op.close() 
'''