# Get our input from the command line
import sys
numbers = sys.argv[1].split(',')
for i in range(0,len(numbers)):
  numbers[i]= int(numbers[i])

def isEven(n) :
  return ((n % 2) == 0)

# Your code goes here
myListEven = []
myListOdd = []

# We are passing in a list of numbers. 
# You need to create 2 new lists in your chart
#    put all odd numbers in one list
#    put all even numbers in the other list
#    output the odd list first 
#    output the even list second
# Tip: use the modulo operator for odd or even. 

# Write your code below
for i in range(0,len(numbers),1):
    if(isEven( numbers[i] ) == 1):
        myListEven.append(numbers[i])
    else:
        myListOdd.append(numbers[i])
        
print(myListOdd)
print(myListEven)

