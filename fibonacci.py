# Write experimental code below
import sys
#number of iterations supplied by user
N = int(sys.argv[1])

# Your code goes here
myincrement = int(1)
i = int(0)

# parameters assume X=0 and Y=1
X = int(0)
Y = int(1)

while i <= N:
    if i == 0:
        answer = X
        print(answer)
    elif i == 1:
        answer1 = Y
        print(answer1)
    else:
        answer2 =  answer + answer1
        print(answer2)
        answer = answer1
        answer1 = answer2
    i = i + myincrement

