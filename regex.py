myString = "Python is named after the Monty " \
           "Python Flying Circus TV show."
aChar = 'V'
def findIt(character, phrase):
  i = 0
  while i < len(phrase):
    if phrase[i] == character:
      return i
    i += 1
  return -1


search Result = findIt(aChar, my String)
if (searchResult == -1):
  print(aChar, 'was found not found')
else:
  print (aChar, 'was found at index position', searchResult)


myString = "Python is named after the Monty " \
           "Python Flying Circus TV show."
mySub = 'ing'


if (myString.find(mySub) == -1):
  print(mySub, 'was not found.')
else:
  print(mySub, 'was found')


if mySub in myString:
  print(mySub, 'was found.')
else:
  print(mySub, 'was not found')

grades = [88, 74, 92, 65, 23, 95, 99, 100, 88, 97]


if 65 in grades:
  print ('65 found in grades list.')
else:
  print('65 not found in grades list.')
  
  