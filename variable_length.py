
# Get the filepath from the command line
import sys
import re
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]
#print(P,":",F,":",L,":",B)

# ---------------------------------------------------------------- 
# Our Helper functions:
# ----------------------------------------------------------------

# Loads the file at filepath 
# Returns a 2d array with the data
# 
def load2dArrayFromFile(filepath):
  # Your code goes here:
  records = []
  #print("load2dArrayFromFile")
  # Open and reada the file.
  myFile = open(P, 'r')
  FileContent = myFile.read()
  myFile.close()
  #print("original files content\n",FileContent, "\n")
  
  #define the expected end of record delimiter
  row_delimiter= '\n'
  #check to see how many lines exist.
  line_count = len(re.findall(row_delimiter,FileContent)) +1
  #parse the file by line into a list
  record_row = re.split(row_delimiter, FileContent) 
  #print(line_count,": full list\n", record_row, "\n")
  


# Searches the 2d array 'records' for firstname, lastname.
# Returns the index of the record or -1 if no record exists
def findIndex(records, firstname, lastname):
  # Your code goes here:
  #print("findIndex")
  IndexValue = int(0)
  for s in range(0,len(records),1):
    #print("Does ",firstname," match ",records[s][0],"?\n")
    if(records[s][0] == firstname):
      #print("Does ",lastname," match ",records[s][1],"?\n")
      if(records[s][1]== lastname):
         IndexValue = s 
  #print("Index Found: ",IndexValue)    
  return(IndexValue)

# Sets the birthday of the record at the given index
# Returns: nothing
def setBirthday(records, IndexValue, newBirthday):
  # Your code goes here:
  #print("setBirthday")
  #print( records[IndexValue][0]," ",records[IndexValue][1]," ",records[IndexValue][2],"\n") 
  records[IndexValue][2] = newBirthday
  #print( records[IndexValue][0]," ",records[IndexValue][1]," ",records[IndexValue][2],"\n") 
  
# Convert the 2d array back into a string
# Return the text of the 2d array
def makeTextFrom2dArray(records):
  String_Dump = str("")
  # Your code goes here:
  #print("makeTextFrom2dArray")
  #How many records? 
  for r in range(0,len(records),1): 
    for c in range(0,len(records[r]),1):
      if c == 0:
        StringRow = records[r][c] + "|"
      elif c == 1:
        StringRow = StringRow + records[r][c] + "|"
      else:
        StringRow = StringRow + records[r][c]
    if r == 0:
      String_Dump = String_Dump + StringRow + "\n"
    elif r == 5:
      String_Dump = String_Dump + StringRow 
    else:  
      String_Dump = String_Dump + StringRow + "\n"
  return(String_Dump)  

# ----------------------------------------------------------------
# 
#  Our main code body, where we call our functions.
#  
# ----------------------------------------------------------------


# Load our records from the file into a 2d array
records= load2dArrayFromFile(P)

# Find out which index, if any, has the name we are hunting
indexWeAreHunting= findIndex(records, F, L)

# Set the birthday record to the one we were passed
setBirthday(records, indexWeAreHunting, B)

# Convert the records into a text string
output= makeTextFrom2dArray(records)

# Your code goes here
# write the text string out to the file
myFile = open(P, 'w')
myFile.write(output)
myFile.close()

myFile = open(P, 'r')
FileContent = myFile.read()
myFile.close()
#print("my change files content\n",FileContent, "\n")


# notes about this. There is an extra space before the first entry in the file " Adam"
# and there is an extra space at the end of the last entry's date "date ".
# to make the output match you have to not put a new line at the end of the last record.