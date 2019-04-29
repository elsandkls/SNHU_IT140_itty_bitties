
# Load our command line arguments
import sys
import re

filepath= sys.argv[1]
S= sys.argv[2]
S_caps = str.upper(S)

# Your code goes here 

# Open the file in filename for reading
file1= open(filepath, 'r')

# Read the entire file into the variable
data = file1.read()

# sub()
results1 = re.sub (S, S_caps, data)
# Print out the contents
print(results1)