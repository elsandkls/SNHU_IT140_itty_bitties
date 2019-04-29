# Get the filepath from the command line
import sys
import re

#import variables
F1= sys.argv[1] 
F2= sys.argv[2]

#print(F1,"\n",F2)
#Read Files in.

#___________ functions _____________
#open files
def openMyFiles(FileName):
  myFile = open(FileName, 'r')
  FileContent = myFile.read()
  myFile.close() 
  return(FileContent)
#print("--------------\n\n") 
#
#write file
def writeMyFiles(FileName, FileContent):
  myFile = open(FileName, 'w')
  myFile.write(FileContent)
  myFile.close()  
#print("--------------\n\n") 
#
def load2dArrayFromFileData(FileContent):
  records = []
  #define the expected end of record delimiter
  row_delimiter= '\n'
  #check to see how many lines exist.
  line_count = len(re.findall(row_delimiter,FileContent))
  #parse the file by line into a list
  record_row = re.split(row_delimiter, FileContent) 
  #print(line_count,": full list\n", record_row, "\n")
  #next we need to parse each line into it's seperate column entries
  #define your column delimiter
  # interestingly "|" causes findall to return null character positions for each character in the string.
  # "\|" returns the delimiter.
  column_delimiter= "\|"
  #check to see how many columns there are, remember it's the number plus 1
  i=0 #test with the first row (0)
  column_count = len(re.findall(column_delimiter,record_row[i]))
  #print("first record list\n", record_row[i], "\n Delimiters counted: ", column_count, "\n")

  #loop through the rows parsing the columns up.
  for i in range(0,line_count,1):
    list_of_columns= re.split(column_delimiter,record_row[i])    
    #print(i," ", str(list_of_columns))
    #add column list to records list, to return to program
    records.append(list_of_columns)
    
  #print(records)  
  return(records)
#----------- next function ----------------
def securityCheck(account_number,account_pin,FileContent):
  security_check = int(0)
  account_selected = int(0)
  #print("securityCheck")
  #print(len(FileContent))
  #print(FileContent)
  for a in range(0,len(FileContent),1):
    # ACCOUNT NUMBER | PIN CODE | BALANCE
    #print(a, " ", account_number, "", account_pin, "", FileContent[a])
    if account_number == FileContent[a][0]:
      # check pin
      if account_pin == FileContent[a][1]: 
        security_check = 1
        account_selected = a
        #print("Confirmed \n")
  #print("--------------\n\n")
  return(security_check, account_selected)
  
  
#----------- next function ----------------
def balanceCheck(account_number,account_pin,FileContent):
  #print("balanceCheck")
  balance_start = 0
  # ACCOUNT NUMBER | PIN CODE | BALANCE
  #print(account_number,"",account_pin,"",FileContent)
  if account_number == FileContent[0]:
    # check pin
    if account_pin == FileContent[1]: 
      #pull balance
      balance_start = FileContent[2]
  #print("--------------\n\n")
  return(balance_start)  
  
#----------- next function ----------------
def balanceAddition(account_number, account_pin, amount_change, FileContent):
  #print("balanceAddition")   
  # ACCOUNT NUMBER | PIN CODE | BALANCE
  #print(account_number,"",account_pin,"",FileContent)
  if account_number == FileContent[0]:
    # check pin
    if account_pin == FileContent[1]: 
      #pull balance
      current_balance = int(FileContent[2])
      amount_change = int(amount_change)
      FileContent[2] = current_balance + amount_change  
  #print("Deposit Completed!\n Current Balance: ",FileContent[2])
  #print("--------------\n\n")
  
#----------- next function ----------------
def balanceSubtraction(account_number, account_pin, amount_change, FileContent):
  #print("balanceSubtraction") 
  # ACCOUNT NUMBER | PIN CODE | BALANCE
  #print(account_number,"",account_pin,"",FileContent)
  if account_number == FileContent[0]:
    # check pin
    if account_pin == FileContent[1]: 
      #pull balance
      current_balance = int(FileContent[2])
      amount_change = int(amount_change)
      if current_balance >=  amount_change :
        FileContent[2] = current_balance  -  amount_change  
      else:
        #print("Insufficient Funds!") 
        boo = 0 
  #print("Withdrawal Completed!\n Current Balance: ",FileContent[2]) 
  #print("--------------\n\n")
  
#----------- next function ----------------

def GenrateFiletoExport(ClientList):
# Generate the string to export back out to the file.
# ACCOUNT NUMBER | PIN CODE | BALANCE
  #print(ClientList)
  FileContent = str("")
  FileRow = str("")
  row_delimiter= '\n'  
  column_delimiter= "|" 
  line_count = len(ClientList)
  #print("--------------\n\n")
  
  for r in range(0,line_count,1):
    column_count = len(ClientList[r])
    FileRow = ""
    for c in range(0,column_count,1): 
      #print(r,":",c,":",column_count,":",ClientList[r][c])
      if c < (column_count-1):
        FileRow = FileRow + str(ClientList[r][c]) + column_delimiter
      else:  
        FileRow = FileRow + str(ClientList[r][c]) 
      #print(FileRow)  
    FileContent = FileContent + FileRow + row_delimiter
  
  #print("--------------\n\n")  
  #print(FileContent)  
  return(FileContent)
  
#----------- end function ----------------
 
  
# Begin Program   
FileContent1 = openMyFiles(F1) 
# Let's look at the contents
# ACCOUNT NUMBER | PIN CODE | BALANCE
#print(FileContent1)  
FileContent1_list = load2dArrayFromFileData(FileContent1)
#print(FileContent1_list)  
#print("--------------\n\n")


FileContent2 = openMyFiles(F2)  
# Let's look at the contents
# 0         1        2                3
# COMMAND | AMOUNT | ACCOUNT NUMBER | PIN CODE
#print(FileContent2)  
FileContent2_list = load2dArrayFromFileData(FileContent2)
#print(FileContent2_list)  
#print("--------------\n\n")

# Begin Automated Sequence
#
##COMMAND will be either add or sub
for i in range(0, len(FileContent2_list),1):
  secure = int(0)
  acc = int(999)
  # make these variables more human readable.
  command_code = FileContent2_list[i][0]
  amount = FileContent2_list[i][1]
  account_num = FileContent2_list[i][2]  # Account Number
  pin_code = FileContent2_list[i][3]  # Pin Code  
  # process command code
  if command_code == "add":
    # If the command is add, you will add to balance 
    secure,acc = securityCheck(account_num,pin_code,FileContent1_list)
    if secure == 1:
      balanceCheck(account_num,pin_code,FileContent1_list[acc])
      balanceAddition(account_num,pin_code,amount, FileContent1_list[acc])
  elif command_code == "sub": 
    # If the command is sub, you will subtract from balance. 
    secure,acc = securityCheck(account_num,pin_code,FileContent1_list)
    if secure == 1:
      balanceCheck(account_num,pin_code,FileContent1_list[acc])
      balanceSubtraction(account_num,pin_code,amount, FileContent1_list[acc])
  else:
    #print("--------------\n\n")
    #print("Exit Program")
    #print("--------------\n\n")
    boo = 0
    
FileContent = GenrateFiletoExport(FileContent1_list)
writeMyFiles(F1, FileContent)    
# # Starting with BALANCE in the account files 
# If you are asked to subtract an amount that would put the account below zero 
# if the pin code you are provided does not match the pin code in the account record, the transaction is ignored.
