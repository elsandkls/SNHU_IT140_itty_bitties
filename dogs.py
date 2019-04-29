def applyDiscount(price, discountRate):
  return price - (price * discountRate)

# Create dictionary template
dog0 = {'Name' : ' ',
        'Age' : 0,
        'Breed' : ' ',
        'Color' : ' ',
        'Boarded' : False,
       'Room' : 0}


# Function to update dog Name
def updateName (theDog, newName):
  theDog['Name'] = newName

# Function to update dog Age
def updateAge (theDog, newAge):
  theDog['Age'] = newAge

# Function to update dog Breed
def updateBreed (theDog, newBreed):
  theDog['Breed'] = newBreed

# Function to update dog Color
def updateColor (theDog, newColor):
  theDog['Color'] = newColor

# Function to board dog
def boardDog (theDog, roomNumber):
![.guides/img/muzz](.guides/img/muzz.png)
  theDog['Room'] = roomNumber
  theDog['Boarded'] = True

# Function to release dog
def releaseDog (theDog):
  theDog['Room'] = 0
  theDog['Boarded'] = False

# Function to print dog record
def printDog (theDog):
  print(theDog)
printDog(dog0)

Output

{'Name': ' ', 'Age': 0, 'Breed': ' ', 'Color': ' ', 'Boarded': False, 'Room': 0}

# Function to print dog record in more readible format
def printDogNicer(theDog):
  print("Welcome to We Pet 'em Kennel \n")
  

  if theDog['Name'] == ' ':
    print("Dog Name: Not provided")
  else:
    print("Dog Name: ", theDog['Name'])
    

  if theDog['Age'] == 0:
    print("Dog Age: Not provided")
  else:
    print("Dog Age: ", theDog['Age'])
    

  if theDog['Breed'] == ' ':
    print("Dog Breed: Not provided")
  else:
    print("Dog Breed: ", theDog['Breed'])
    

  if theDog['Color'] == ' ':
    print("Dog Color: Not provided")
  else:
    print("Dog Color: ", theDog['Color'])
    

  if theDog['Boarded'] == True:
    print("Boarding Status: Currently in Room", theDog['Room'])
  else:
    print("Boarding Status: Not Boarded")

releaseDog(dog1)
printDogNicer(dog1)


Welcome to We Pet 'em Kennel


Dog Name: Muzz
Dog Age: 9
Dog Breed: Shar Pei / Golden Mix
Dog Color: Blonde
Boarding Status: Not Boarded

