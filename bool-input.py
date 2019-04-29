

# Get our boolean values from the command line
import sys
isCold= sys.argv[1] == 'True'
isRainy= sys.argv[2] == 'True'

# Your code goes here
if isCold and isRainy:
  print("cold and rainy")
elif isCold and not isRainy:
  print("cold and dry")
elif not isCold and isRainy:
  print("warm and rainy")
elif not isCold and not isRainy:
  print("warm and dry")
else:
  print("cold")
  print("warm")
  print("rainy")
  print("dry")


