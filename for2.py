# We will pass in a value, N. 
# N can be positive or negative.

if N >= 0:
    # If N is positive then output all values from N down to and excluding 0.
    stop = int(0 -1)
    start = int(N)
    myincrement = int(-1)
else:
    # If N is negative, then output every value from N up to and excluding 0.
    stop= int(0 +1)
    start = int(N)
    myincrement = int(+1)

print 'Start: ', start, '\n'
print 'Stop: ', stop , '\n'

for i in range(start, stop, myincrement):
    print(i)


