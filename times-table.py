# Write experimental code below
import sys
N = int(sys.argv[1])

# Your code goes here
# We will pass in a value, N. 
# N can be positive or negative.

# Output the times table for that number from 1 to 12.
start = int(1)
stop = int(13)
myincrement = int(+1)
answer = int(0)

print 'Start: ', start, '\n'
print 'Stop: ', stop , '\n'

for i in range(start, stop, myincrement):
    answer = N * i
    print answer

