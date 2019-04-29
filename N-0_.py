# Write experimental code below
print ("Your experiemental code")

# Get N from the command line
import sys
N = int(sys.argv[1])

# Your code goes here
# We will pass in a value, N. 
# You should output every positive value from N down to and including 0.

stop = int(0 -1)
start = int(N)

print 'Start: ', start, '\n'
print 'Stop: ', stop , '\n'

for i in range(start, stop, -1):
    print(i)


