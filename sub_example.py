import re
cerseiSpeech = "The Mad King's daughter has ferried an arm of savages to " \
               "our shores, mindless unsullied soldiers who would destroy " \
               "your castles and your holdfasts, Dothraki heathens who " \
               "will burn your villages to the ground, rape and enslave " \
               "your women, and butcher your children without a second " \
               "thought... You remember the mad king, you remember the " \
               "horrors he inflicted on his people. His daughter is no " \
               "different. In Essos her brutality is already legendary. " \
               "She crucified hundreds of noblemen in Slavers Bay. And " \
               "when she got bored of that, she them to her dragons. " \
               "It is my solemn duty to protect the people and I will, but " \
               "I need your help my lords. We must stand together, all of " \
               "us, if we hope to stop her."


# sub()
results1 = re.sub ('her', 'HER', cerseiSpeech)
results2 = re.sub ('she', 'SHE', results1)
print(results2)


#my example


# Get the filepath from the command line
import sys
import re
# You will be provided a file path for input I
I= sys.argv[1] 
file1= open(I, 'r')
# You will be provided a file path for output O 
O= sys.argv[2] 
file2= open(O, 'w')
# You will be provided a string S
S= sys.argv[3]
# You will be provided a string T
T= sys.argv[4]

# Your code goes here 
# Read the contents of I 
data_Read = file1.read()
# Replacing each occurrence of S with T 
data_Write = re.sub (S, T, data_Read)
# Write the resulting information to file O.
file2.write(data_Write)
# You should replace O if it already exists.

# close the files
file1.close() 
file2.close() 
