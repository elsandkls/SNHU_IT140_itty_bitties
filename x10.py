# Get our input from the command line
import sys
M= int(sys.argv[2])
N= int(sys.argv[3])

# convert strings to integers
numbers= sys.argv[1].split(',')
for i in range(0, len(numbers)):
  numbers[i]= int(numbers[i])

# Your code goes here
# numbers now contains the list of integers 
# You should multiply every Nth element by M. 
# (do not multiply the 0th element)
#       
MyIncrement = int(1)
CheckIt = int(N)

# Write your code below
for i in range(0,len(numbers),1):
    print(MyIncrement)
    if(MyIncrement == CheckIt):
        numbers[i] = numbers[i] * M
        CheckIt = CheckIt + N
        print("updated it")
    MyIncrement = MyIncrement +1
    
print(numbers)

