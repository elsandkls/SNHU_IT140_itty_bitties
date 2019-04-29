
# Get our list from the command line
import sys
numbers = sys.argv[1].split(",")
num_total = int(0)

# Your code goes here
for i in range(0, len(numbers)):
  num_total = num_total + int(numbers[i])
  
print (num_total)


