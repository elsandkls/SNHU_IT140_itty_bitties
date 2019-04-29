# Get our list from the command line arguments
import sys
numbers= sys.argv[1:]

# Convert the command line arguments into 2d list
for i in range(0,len(numbers)): 
  numbers[i]= numbers[i].split(',')
  
# Write your code below

# We will pass in a 2 dimensional list of numbers.
# add up all the numbers in each row 
# output the row total 
# output the grand total of all rows
# You need to create 2 new lists in your chart
rowTotal = []
problemTotal = int(0)

# Write your code below
for i in range(0,len(numbers),1):
    rowTotal.append(0)
    for x in range(0, len(numbers[i]),1):
        print(i, x, numbers[i][x])
        rowTotal[i] = int(numbers[i][x]) + rowTotal[i]
        problemTotal = int(numbers[i][x]) + problemTotal
    print(rowTotal[i])
print(problemTotal)

