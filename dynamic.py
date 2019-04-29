# Get our arguments from the command line
import sys
A= int(sys.argv[1])
B= int(sys.argv[2])

# Write your code below
myList = []
myString = ""

# We pass in 2 numbers, A and B. 
# You should create a list with A rows and B columns.
# You should then populate each cell like this 
# R0C0, R0C1, R0C2 etc.

for i in range(0,A,1):
    myList.append([])
    for x in range(0,B,1):
        myList[i].append("")

i = 0
x = 0

for i in range(0,A,1):
    print(i)
    for x in range(0,B,1): 
            myList[i][x] = "R" + str(i) + "C" + str(x) 
            print(i,x,myList[i][x])
print(myList)

