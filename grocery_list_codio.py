#Grocery List Script
#
 
# create an empty dictionary
grocery_item = {}
# create an empty list
grocery_history = []

# create a variable - define action
stop = 'go'

# create while loop
# While loops
while stop != 'q':

  #collect customer inputs
  item_name = input("Item name:\n") 
  quantity = input("Quantity purchased:\n")    
  cost = input("Price per item:\n") 
  
  #format inputs and store in a dictionary
  # Adding and removing key–value pairs
  grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)} 
  
  #Add customer input to list
  # Adding data to a list
  grocery_history.append(grocery_item)

  #ask user if they want to continue
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")


# define variables
grand_total = int(0)
item_total = int(0)   

#loop through the grocery history/cart(dictionary) 
## Index-based (range) for loops
for i in range(0,len(grocery_history),1):

  #calculate per item total
  # Accessing values in a list
  # Accessing values using keys
  item_total =  grocery_history[i]['number'] * grocery_history[i]['price']

  #calculate the subtotal
  grand_total = grand_total + item_total
  
  #output line item with item total
  print(grocery_history[i]['number'], grocery_history[i]['name'], "@", '${:,.2f}'.format(grocery_history[i]['price']), " ea ", '${:,.2f}'.format(item_total))
  
  #clear out the variable by setting it to 0
  item_total = int(0)
  
#print out the amount owed or grand total
print("Grand Total: ",'${:,.2f}'.format(grand_total))