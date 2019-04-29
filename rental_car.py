import sys 

#Assigning a numerical value 
rentalPeriod = int(0) 

#Collect customer input
##Collecting string input
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
   
if (rentalCode == "B"):
  #Collecting string input
  rentalPeriod = input("Number of Days Rented:\n") 
elif(rentalCode == "D"):
  #Collecting string input
  rentalPeriod = input("Number of Days Rented:\n") 
elif(rentalCode == "W"):
  #Collecting string input
  rentalPeriod = input("Number of Weeks Rented:\n") 
else:
  print("End Program") 

# predefined variables for calculations
# Modifing the variable type
rentalPeriod = int(rentalPeriod) 
# Assigning a numerical value 
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00 
 
# Calculate the customer's base rental sub total  
if (rentalCode == 'B'):
  #Modifying variables with data-type-appropriate operators
    baseCharge = int(rentalPeriod) * budgetCharge
elif (rentalCode == 'D'):
  #Modifying variables with data-type-appropriate operators
    baseCharge = int(rentalPeriod) * dailyCharge
elif (rentalCode == 'W'):
  #Modifying variables with data-type-appropriate operators
    baseCharge = int(rentalPeriod) * weeklyCharge
# branch else 
else:
  print("End Program")  

# Collect customer input and calculate total miles
#Assigning a string value 
odoStart = str("0")
odoStart = input("Starting Odometer Reading:\n")   

odoEnd = str("0") 
odoEnd = input("Ending Odometer Reading:\n") 

totalMiles = int(0)
#Modifying variables with data-type-appropriate operators
totalMiles = int(odoEnd) - int(odoStart)

#Calculate the customers millage fee if any
# branch if
if(rentalCode == "B"):
  #Modifying variables with data-type-appropriate operators
  mileCharge = totalMiles * 0.25 
# branch elif  
elif(rentalCode == "D"): 
  #Modifying variables with data-type-appropriate operators
  averageDayMiles = totalMiles/rentalPeriod
  # branch if
  if(averageDayMiles <= 100):
    extraMiles = 0   
  # branch elif  
  elif(averageDayMiles > 100):
    extraMiles = averageDayMiles - 100 
  # branch else  
  else:
    extraMiles = 0
  mileCharge = .25 * extraMiles #* rentalPeriod

# branch elif 
elif(rentalCode == "W"): 
  #Modifying variables with data-type-appropriate operators
  averageWeekMiles = totalMiles/ rentalPeriod
  # branch if
  if(averageWeekMiles <= 900):
    mileCharge = 0  
  # branch elif  
  elif(averageWeekMiles > 900):
    mileCharge = 100 
  # branch else  
  else:
    mileCharge = 0 
# branch else  
else:
  print("End Program")  

# Calculate the amount due.
# declaring a variable an int
amtDue = int(0)
#Modifying variables with data-type-appropriate operators
amtDue = baseCharge + mileCharge 

# Display a customer summary
#Rental Summary
print("Rental Summary")
#Rental Code:        The rental code
print("Rental Code:\t",rentalCode)
#Rental Period:      The number of days the vehicle was rented
print("Rental Period:\t",rentalPeriod)
#Starting Odometer:  The vehicle's odometer reading at the start of the rental period
print("Starting Odometer:\t",odoStart)
#Ending Odometer:    The vehicle's odometer reading at the end of the rental period
print("Ending Odometer:\t",odoEnd)
#Miles Driven:       The number of miles driven during the rental period
print("Miles Driven:\t",totalMiles)
#Amount Due:         The amount of money billed displayed with a dollar sign and
#                    rounded to two digits. For example, $125.99 or $43.87                   
print("Amount Due:\t",'${:,.2f}'.format(amtDue))

#End program