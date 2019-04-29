
# Get the filepath from the command line
import sys
import re
P= sys.argv[1]  #input_filename 
F= sys.argv[2]  #FirstName
L= sys.argv[3]  #LastName
B= sys.argv[4]  #New Birthday 
O= "output.txt"  #output_filename

# security parsing. Add a space to the end of F and L
F = F +" "
L = L +" "

# open the filename
file1= open(P, 'r')
data = file1.read()
# close the files
file1.close() 

#print(data)
#print("\n")  
String_Dump = str("")

# Load the fixed length record file in P, search for F,L in the first and change birthday to B.
# Hint: Each record is at a fixed length of 16
recordLength= (16*2)+8 # each line is 16, each individual field can vary inside the line.
start= 0
databaseEntries= [] 
recordEntries= [] 
recordFNLNDB = str()  

# use the substring function to read all the records from the file and parse into lines
while( (len(data) - start) >= recordLength):
  record= data[start:start + recordLength]
  databaseEntries.append(record)
  #print(record)
  start+= recordLength
#print("\n")  

# print out all of our records
for i in range(0,len(databaseEntries)):
  #print("Last Name Match")  
  data = databaseEntries[i]
  #print("Last Name Match")
  recordFN= data[0:0 + 16] 
  #print(recordFN)
  recordLN= data[16:16 + 16]
  #print(recordLN)
  recordBD= data[32:32 + 8] 
  #print('Record '+ str(i) +': ('+databaseEntries[i]+')')
  # check for match
  response1 = re.findall(F, recordFN)
  #print(response1)
  
  if(len(response1) == 1):
    #print("First Name Match")
    response2 = re.findall(L, recordLN)
    #print(response2)
    
    if(len(response2) == 1):
      #print("Last Name Match") 
      # both match change birthdate
      databaseEntries[i] = "" + recordFN + "" + recordLN + "" + B + ""
      #print(databaseEntries[i])
    #else:
     #print("Last Name: No Match")
  #else:
    #print("First Name: No Match")
    
  String_Dump = String_Dump + databaseEntries[i]
     
#String_Dump = String_Dump + "\n"    
#print("\n")  
# open the filename
file1= open(P, 'w') 
#file1.write("\n")
file1.write(String_Dump)  
# close the files
file1.close() 

