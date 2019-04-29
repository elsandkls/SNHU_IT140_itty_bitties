
# Get our input from the command line
import sys
N= int(sys.argv[2])

# Convert the list of strings into integers
numbers= []
for i in sys.argv[1].split(","):
  if(i.isdigit()):
    numbers.append(int(i))
# numbers now contains the list of integers
                   
# Write your code below
for i in range(0,len(numbers),1):
  if(numbers[i] == N):
    print(i) 
    break
  else:
    #nada
    print(" ")
