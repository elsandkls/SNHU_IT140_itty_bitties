
# Creating a 2D list
desks= [
  ['Adam', 'Ben', 'Carl', 'David'],
  ['Edward', 'Frank', 'Georgia', 'Helen'],
  ['Isabelle', 'Joan', 'Kelly', 'Linda']
]

# Looping through both dimensions
for row in desks:
  print('this row has ' + str(len(row)) + ' items')
  
  for col in row:
    print(col)
  
  print('---')

