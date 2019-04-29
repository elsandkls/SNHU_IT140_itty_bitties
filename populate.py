# Get N from the command line
import sys
N= int(sys.argv[1])
myValue = int(0)

# Your code goes here.....

# Requirements
# Create an empty list 
# Use a loop 
# Populate the list with N elements.
# Set each list element to the index (N) multiplied by 10.
# N value of 0, should return an empty list.
# Proceed

myList = []
for i in range(0,N,1):  
  myValue = 10 * i  
  myList.append(myValue)  

  
print(myList)

