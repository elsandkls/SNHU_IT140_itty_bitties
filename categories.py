
# Get the age from the command line
import sys
age= int(sys.argv[1])

# Your code goes here
if age >= 6 and age <= 11:
  print("primary school")
elif age >= 12 and age <= 18:
  print("secondary school")
else:
  print("NA")


