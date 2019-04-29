# Write experimental code below
import sys
N = int(sys.argv[1])

# Your code goes here
# We will pass in a value, N. 
# X factorial solution 

start = int(N)
stop = int(1)
myincrement = int(-1)
answer = int(1)

#print 'Start: ', start, '\n'
#print 'Stop: ', stop , '\n'

for i in range(start, stop, myincrement):
    answer = i * answer 
    #print answer,' ',N,' ',i

print answer

