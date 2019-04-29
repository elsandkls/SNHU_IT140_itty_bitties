
# Get our lists from the command line
# It's okay if you don't understand this right now
import sys
list1 = sys.argv[1].split(',')
list2 = sys.argv[2].split(',')


#
# Print the lists.
# 
# Python puts '[]' around the list and seperates the items
# by commas.
print(list1)
print(list2)

#
# Note that this list has three different types of items
# in the container: an Integer, a String, and a Boolean.
# 
list3 = [1,"red", True]
print(list3)

strList = ['Alice', 'Shahneila', 'Bobx, 'Tariq']
numList = [1, 3.141, 5, 17.1, 100]
numList = []
numList.append(4)


# create a list
aList = [ 'Alice', 'Shahneila', 'Bob', 'Tariq' ]

print(aList)

# change the second element
aList[1] = 'Sean'

print(aList)
# create an empty list
numList = []

# append some items to the empty list
numList.append(1)
numList.append(2)
numList.append(4)

print(numList)

# insert an element at a specific index
numList.insert(2, 3)

print(numList)

aString = '12345'
# use the len() function to get the length of a string
print('the string has a length of:')
print(len(aString))

aList = [1,2,3,4,5]
# you can also use the len() function to get the length of a list
print('the list has a length of:')
print(len(aList))

myList = [1,3,5,7,9]

stop = len(myList)
print('the list has ' + str(stop) + ' elements')

aRange = range(0, stop)

for i in aRange:
  print(myList[i])

  
# short version  

print('a shorter way of creating ranges for looping')

for i in range(0, len(myList)):
  print(myList[i])
  

# display every second item

print('range step of 2')

for i in range(0, len(myList), 2):
  print(myList[i])


