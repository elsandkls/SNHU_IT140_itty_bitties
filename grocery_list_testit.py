# Grocery List Project                 

# name, cost, quantity, available in the store -- groceries
#     i. Identify: Creating dictionaries 
grocery_list={'category':'meat', 'products':[
{'name': 'eggs', 'cost': 5, 'quantity': 1,'defmeasure':'dozen'},
{'name': 'breakfast sausage roll', 'cost': 5, 'quantity': 1,'defmeasure':'8 oz'},
{'name': 'breakfast sausage patties', 'cost': 5, 'quantity': 1,'defmeasure':'8 oz'},
{'name': 'bacon thick', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'bacon thin', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'steak beef', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'roast beef', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'ground beef', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'sausage links', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'chicken breast', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'chicken wings', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'chicken legs', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'},
{'name': 'chicken whole', 'cost': 5, 'quantity': 1,'defmeasure':'2 lb'},
{'name': 'fish fillets', 'cost': 5, 'quantity': 1,'defmeasure':'16 oz'}]
} 

i = int(0)
x = int(0)

print("grocery list")
print(grocery_list) 

print("grocery list category")
print(grocery_list['category'])  

print("grocery list products")
print(grocery_list['products']) 

print("grocery list products name")
print(grocery_list['products'][i]['name']) 
print("grocery list products cost")
print(grocery_list['products'][i]['cost']) 
print("grocery list products quantity")
print(grocery_list['products'][i]['quantity']) 
print("grocery list products defmeasure")
print(grocery_list['products'][i]['defmeasure']) 

for i in (0, len(grocery_list['products'][0]), 1):
    print("Name: ", str.capitalize(grocery_list['products'][i]['name']), "Price:", grocery_list['products'][i]['cost'], "Quantity: ", grocery_list['products'][i]['quantity'], "Size: ", grocery_list['products'][i]['defmeasure'])  

print("\n\n")

