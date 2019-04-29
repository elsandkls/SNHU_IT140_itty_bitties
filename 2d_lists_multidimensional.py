
# Create an empty array first
# This gives us our first dimension
data = []

# our list dimensions 
rows = 5
cols = 4

# We work through the rows first, dimension 1
for x in range(0, rows):
  # Append a new list to create the 2nd dimension
  data.append([])
  
  for y in range(0, cols):
    # Now we can append cells to the row
    data[x].append(str(x) + ',' + str(y))

print(data)

