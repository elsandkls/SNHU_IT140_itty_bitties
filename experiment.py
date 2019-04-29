# Write experimental code below
print ("Your experiemental code")

# Get N from the command line
import sys
N = int(sys.argv[1])

# Your code goes here
# We will pass in a value, N. 
# You should write a program that outputs all values from 0 up to an including N.
start = int(0)
stop = int(N + 1)

print 'Start: ', start, '\n'
print 'Stop: ', stop , '\n'

for i in range(start, stop, +1):
    print(i)



