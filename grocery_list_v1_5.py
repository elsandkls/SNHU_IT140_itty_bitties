# Grocery List Project 

# example of a function:
def printCategory(category_list):
    i = int(1)
    stop = len(category_list) -1
    #     i.   Identify: Item-based for loops
    while i <= stop:   
        #iii. Identify: Accessing values in a list
        print(i, str.capitalize(category_list[i]))
        i= i+1; 
    print("\n")
    return (0)

def printCustomerCart(customer_grocery_list): 
    #     ii.  Identify: Index-based (range) for loops  
    for i in range(0,len(customer_grocery_list),1):
        print(i, customer_grocery_list[i])
        # add pulling data from grocery_list_dictionary using the list to match the Uindex.
    print("\n")
    return (0)

def printGroceryList(grocery_list_dictionary, category_selection, category_list):
    k = int(0)
    k = len(grocery_list_dictionary)
    if(category_selection != 0):
        print("Category: \t ", str.capitalize(category_list[category_selection]))
        print("Name: \t\t\t Price: \t Quantity: \t Size: \t ")  
        for i in range (0,k,1): 
            if(category_list[category_selection] == grocery_list_dictionary[i]['category'] ): 
            #     iii. Identify:  Accessing values using keys
                print(grocery_list_dictionary[i]['Uindex'], str.capitalize(grocery_list_dictionary[i]['name']), "\t\t", grocery_list_dictionary[i]['cost'], "\t\t", grocery_list_dictionary[i]['quantity'], "\t\t\t", grocery_list_dictionary[i]['defmeasure'])  
    else:
        print("UID:\t Cat:\t Name: \t\t\t Price: \t Q: \t Size: \t ")  
        for i in range (0,k,1):  
            #     iii. Identify:  Accessing values using keys
            print(grocery_list_dictionary[i]['Uindex'], str.capitalize(grocery_list_dictionary[i]['category']),  str.capitalize(grocery_list_dictionary[i]['name']), "\t\t", grocery_list_dictionary[i]['cost'], "\t\t", grocery_list_dictionary[i]['quantity'], "\t\t\t", grocery_list_dictionary[i]['defmeasure'])  

 
    print("\n")
    return (0)
 
 
def printMenu(menu_content):
    i = int(1)
    stop = len(menu_content) -1
    #     i.   Identify: Item-based for loops
    while i <= stop:   
        #iii. Identify: Accessing values in a list
        print(menu_content[i]) 
        i= i+1; 
     
    print("\n")
    return (0) 
 
  
# Create dictionary with a grocery list.  
# Assign the dictionary to the variable grocery_list
#     i. Identify: Creating dictionaries 
category_list =  ['','dairy','meat','bakery','deli','canned','frozen','fruit','veggies','Misc']                   

# name, cost, quantity, available in the store -- groceries
#     i. Identify: Creating dictionaries 
grocery_list_dictionary = [{'Uindex':101, 'category':'dairy', 'name':'whole milk','cost':2,'quantity':1,'defmeasure':'1 gal' },
{'Uindex' : 102, 'category':'dairy', 'name':'creamer','cost':2,'quantity':1,'defmeasure':'64 fl oz' },
{'Uindex' : 103, 'category':'dairy', 'name':'heavy cream','cost':2,'quantity':1,'defmeasure':'1 qt' },  
{'Uindex' : 107, 'category':'meat', 'name': 'eggs', 'cost': 5, 'quantity': 1,'defmeasure':'dozen'},
{'Uindex' : 108, 'category':'meat', 'name': 'sausage roll', 'cost': 5, 'quantity': 1,'defmeasure':'8 oz'}, 
{'Uindex' : 110, 'category':'meat', 'name': 'bacon thick', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},  
{'Uindex' : 116, 'category':'meat', 'name': 'chicken breast', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'Uindex' : 122, 'category':'bakery', 'name': 'dinner rolls', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'Uindex' : 123, 'category':'bakery', 'name': 'cupcakes', 'cost': 5, 'quantity': 1,'defmeasure':'tray (dozen)'},   
{'Uindex' : 128, 'category':'deli', 'name': 'sliced turkey', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'Uindex' : 133, 'category':'deli', 'name': 'sliced salami', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'Uindex' : 134, 'category':'canned', 'name': 'pickles', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},  
{'Uindex' : 147, 'category':'canned', 'name': 'yams', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'Uindex' : 140, 'category':'frozen', 'name': 'ice cream cake', 'cost': 5, 'quantity': 1,'defmeasure':'gal'},
{'Uindex' : 151, 'category':'frozen', 'name': 'custard pie', 'cost': 5, 'quantity': 1,'defmeasure':'1'}, 
{'Uindex' : 156, 'category':'fruit', 'name': 'oranges',  'cost': 5, 'quantity': 1,'defmeasure':'bag'}, 
{'Uindex' : 169, 'category':'fruit', 'name': 'apples', 'cost': 5, 'quantity': 1,'defmeasure':'bag'}, 
{'Uindex' : 175, 'category':'veggies', 'name': 'pumpkin', 'cost': 5, 'quantity': 1,'defmeasure':'1 lb'},
{'Uindex' : 176, 'category':'veggies', 'name': 'green beans', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'Uindex' : 177, 'category':'veggies', 'name': 'corn cob', 'cost': 5, 'quantity': 1,'defmeasure':'bag'}]

# note to self, watch out for the lists, they are poitners, they are not unique in memory.
# Create dictionary with a customer grocery list.  
# Assign the dictionary to the variable customer_grocery_list
# name, cost, quantity -- customers shopping cart - groceries
#     i. Identify: Creating lists 
customer_grocery_list=[]
question_count = int(3)

# menu for a simple grocery list and checkout.. 
#     i. Identify: Creating lists 
menu_main = [ "   ",
"####################################",
"###  Grocery List Script   ###",
"####################################",
"  1. List and Select available categories. ", 
"  2. List groceries. ",
"  3. Add groceries to shopping cart. ",
"  4. Remove groceries from shopping cart. ",
"  5. Check out.",
"  7. Exit program. ", 
"####################################",
"####################################",
" ** Admin Access ** 0 ",
"####################################",
"####################################",
" "]
menu_admin= [ "   ",
"####################################",
"### Admin Options   ###",
"####################################",
"  1. Update item price. ",   
"  2. Delete item from list. ",   
"  3. Add item to list. ",   
"####################################",
" "]

# create simple int variable 
menu_start = int(0)
menu_stop = len(menu_main)
menu_myinc = int(1)
menu_selection = int(0)
admin_menu_selection = int(0)
category_selection = int(0)
category_name = str()
new_price = float()

#menu system
# 1. User Input
#iii. Identify:  While loops
while menu_selection <= 6: 
    #print menu options 
    printMenu(menu_main)

    menu_selection = input('Enter your seletion (1,2,3,4,5,6): ')
    menu_selection = int(menu_selection) 

    if (menu_selection == 0): 
        #print menu options 
        printMenu(menu_admin)
    
        admin_menu_selection = input('Enter your seletion (1,2,3): ')
        admin_menu_selection = int(admin_menu_selection) 
        print('%i selected \n' % admin_menu_selection) 
        if (admin_menu_selection == 1): 
            # Change items price
            printGroceryList(grocery_list_dictionary,0, category_list)
            
            # ask for produt identifier       
            grocery_selection = input('Which item do you want to update? : ')
            print("Updating item: ",grocery_selection)
            # ask for new price
            new_price = input('What is the new price? : ')
            print("Price changing to: ",new_price)
            # update the list with the new price.                 
            #     iv. Identify: Modifying values in a list  
            for i in range(0,len(grocery_list_dictionary),1):
                grocery_selection = int(grocery_selection) 
                if (grocery_list_dictionary[i]['Uindex'] == grocery_selection):
                    grocery_list_dictionary[i]['cost'] = new_price 
                    print("\n\n")        
                            
        elif (admin_menu_selection == 2):
            # Delete item from list.for i in range(menu_start,len(category_list),menu_myinc):       
            printGroceryList(grocery_list_dictionary,0, category_list)
            
            # ask for produt identifier       
            grocery_selection = input('Which item do you want to delete? : ')
            print("Delete item: ",grocery_selection)
            grocery_selection = int(grocery_selection) 
            # ask for new price
            status_check = input('Confirm you want to delete this item? (Y/N) : ')
            print("Confirmed: ",status_check)
            # update the list with the new price.                 
            #     iv. Identify: Modifying values in a list  
            for i in range(0,len(grocery_list_dictionary),1):
                if (grocery_list_dictionary[i]['Uindex'] == grocery_selection):
                    del grocery_list_dictionary[i]
                    #     ii. Identify: Removing key:value pairs
            
            for i in range(0,len(category_list),1):
            # print grocery list
                printGroceryList(grocery_list_dictionary,i, category_list) 
            print("\n\n")        
    
        elif (admin_menu_selection == 3):
            # Add item to list      
            #     ii. Identify: Adding and removing key:value pairs 
            printGroceryList(grocery_list_dictionary,0, category_list)
             
            # ask for new price
            status_check = input('Do you want to add a new item? (Y/N) : ')
            print("Confirmed: ",status_check)
            # update the list with the new price.                 
            #     iv. Identify: Modifying values in a list 
            running_high_number = int(0)
            for i in range(0,len(grocery_list_dictionary),1):
                if (grocery_list_dictionary[i]['Uindex'] > running_high_number):
                    running_high_number = grocery_list_dictionary[i]['Uindex']
                        
            #     ii. Identify: Adding key:value pairs
            my_temp_dict = { }
            my_temp_dict['Uindex'] = running_high_number +1
            my_temp_dict['name'] = input('Product name? : ')   
            my_temp_dict['cost'] = input('Product Cost? : ')  
            my_temp_dict['quantity'] = input('Product Quanity? : ')  
            my_temp_dict['defmeasure'] = input('Product Size? : ')  
            my_temp_dict['category'] = "Misc"            
            print(my_temp_dict)  
            grocery_list_dictionary.append(my_temp_dict) 
            print("\n")
            printGroceryList(grocery_list_dictionary,0, category_list) 
            print("\n\n") 
        
    elif (menu_selection == 1):     
        # 2. Loop through the category list 
        printCategory(category_list)
        category_selection = input('Select a catagory: ')
        print(category_selection)
        category_selection = int(category_selection)

    elif (menu_selection == 2):
        # 2. Loop through the grocery list 
        printGroceryList(grocery_list_dictionary,category_selection, category_list)

    elif (menu_selection == 3):
        sub_menu_selection = str("Y")
        while sub_menu_selection == "Y": 
            # 2. Loop through the grocery list 
            printGroceryList(grocery_list_dictionary,category_selection, category_list) 
            question_count = int(0)
            while question_count <= 3: 
                question_count = question_count + 1  
                grocery_selection = input('Add to cart: ')
                print("Adding item: ",grocery_selection)
                #ii. Identify: Adding data from a list
                customer_grocery_list.append(grocery_selection) 
            
            sub_menu_selection = input('Continue adding items? (Y/N) ') 
 
    elif (menu_selection == 4): 
        # remove groceries from cart.  
        # print cart
        printCustomerCart(customer_grocery_list)
        # ask customer which to remove
        grocery_selection = input('Remove from cart: ')
        print(grocery_selection)
        # remove selection.
        #ii. Identify: Removing data from a list
        customer_grocery_list.remove(grocery_selection) 
        # ask customer if they would like to remove another
                 
    elif (menu_selection == 5): 
        # 3. Provide output to the console 
        customer_sub_total = int(0)
        product_index = int(0)
        # print shopping cart contents
        printCustomerCart(customer_grocery_list) 
        #     iii. Identify: Accessing values in a list
        #     iv. Identify: Modifying values in a list  
        for x in range(0,len(customer_grocery_list),1):
            product_index = int(customer_grocery_list[x])
            for i in range(0,len(grocery_list_dictionary),1): 
                if (grocery_list_dictionary[i]['Uindex'] == product_index):
                    customer_sub_total = customer_sub_total + grocery_list_dictionary[i]['cost']
                    # access product totals and calculate the sub total
        # output total to customer
        customer_sub_total = float(customer_sub_total) 
        print("Cart total: ", '${:,.2f}'.format(customer_sub_total ))
        # write the sub total to customer list for later use
        # Do we need to alculate tax on food items for this program? 
        # Ohio has no food tax (my state).

    else:
        print("End of program.")


 
