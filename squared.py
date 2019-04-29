# Write experimental code below
import sys
N = int(sys.argv[1])

# Your code goes here
# We will pass in a value, N. 
# X squared solution 

start = int(0)
stop = int(N+1)
myincrement = int(+1)
answer = int(0)

for i in range(start, stop, myincrement):
    answer = (i * i) + answer

print answer

