# Grocery List Project                 

# Create dictionary with a grocery list.  
# Assign the dictionary to the variable grocery_list
#     i. Identify: Creating dictionaries 
category_list =  ['','dairy','meat','bakery','deli','canned','frozen','fruit','veggies']     
 
i = int(0)
x = int(0) 

j = len(category_list)
print("cl_len:", j)
print("category list")
print(category_list)   
print("\n\n") 

i = int(1)
stop = len(category_list) -1
while i <= stop:   
    print(i, " String: ",  str.capitalize(category_list[i]))
    i= i+1; 
print("\n\n") 

# name, cost, quantity, available in the store -- groceries
#     i. Identify: Creating dictionaries 
grocery_list=[{'category':'dairy', 'name':'whole milk','cost':2,'quantity':1,'defmeasure':'1 gal' },
{'category':'dairy', 'name':'creamer','cost':2,'quantity':1,'defmeasure':'64 fl oz' },
{'category':'dairy', 'name':'heavy cream','cost':2,'quantity':1,'defmeasure':'1 qt' }, 
{'category':'meat', 'name': 'eggs', 'cost': 5, 'quantity': 1,'defmeasure':'dozen'},
{'category':'meat', 'name': 'breakfast sausage roll', 'cost': 5, 'quantity': 1,'defmeasure':'8 oz'}, 
{'category':'meat', 'name': 'roast beef', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'category':'bakery', 'name': 'dinner rolls', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'category':'bakery', 'name': 'cupcakes', 'cost': 5, 'quantity': 1,'defmeasure':'tray (dozen)'},         
{'category':'bakery', 'name': 'chocolate muffins', 'cost': 5, 'quantity': 1,'defmeasure':'tray (dozen)'}, 
{'category':'deli', 'name': 'sliced turkey', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'category':'deli', 'name': 'sliced chicken', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'category':'deli', 'name': 'sliced ham', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'category':'canned', 'name': 'pickles', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'category':'canned', 'name': 'carrots', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'category':'canned', 'name': 'green beans', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}, 
{'category':'frozen', 'name': 'ice cream cake', 'cost': 5, 'quantity': 1,'defmeasure':'gal'},
{'category':'frozen', 'name': 'custard pie', 'cost': 5, 'quantity': 1,'defmeasure':'1'}, 
{'category':'fruit', 'name': 'oranges',  'cost': 5, 'quantity': 1,'defmeasure':'bag'}, 
{'category':'fruit', 'name': 'blue berries', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'category':'fruit', 'name': 'strawberriess', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'category':'veggies', 'name': 'bell pepper', 'cost': 3, 'quantity': 1,'defmeasure':'bag'}, 
{'category':'veggies', 'name': 'green beans', 'cost': 5, 'quantity': 1,'defmeasure':'bag'},
{'category':'veggies', 'name': 'corn cob', 'cost': 5, 'quantity': 1,'defmeasure':'bag'}]


k = int(0)
i = int(0)
name_string = str()
k = len(grocery_list)  
for i in range (0,k,1):   
    print( name_string )
    print("Category: ", str.capitalize(grocery_list[i]['category']))
    print("Name: ",  str.capitalize(grocery_list[i]['name'] ) )
    print("Price: ", grocery_list[i]['cost'])
    print("Quantity: ", grocery_list[i]['quantity'])
    print("Size: ", grocery_list[i]['defmeasure'])  
print("\n\n")

print(grocery_list[1]['category'])   
print(grocery_list[1]['name'])  
print(grocery_list[1]['cost'])  
print(grocery_list[1]['quantity']) 
print(grocery_list[1]['defmeasure']) 
print("\n\n")
