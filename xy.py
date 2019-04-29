# Write experimental code below
import sys
X = int(sys.argv[1])
Y = int(sys.argv[2])

# Your code goes here
# We will pass in a value, N. 
# X squared solution 

start = int(1)
stop = int(Y)
myincrement = int(+1)
answer = int(X)

for i in range(start, stop, myincrement):
    answer =  X * answer


print answer

