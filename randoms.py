import random
print(random.randint(1, 10))


#
# Randomization
#
import random
answer = (random.randint(1, 10))
guess = int(input('Enter Your Guess: '))
if answer == guess:
  print ("You win.")
else:
  print("You are wrong. Correct answer was ", answer)

Enter Your Guess: 3
You are wrong. Correct answer was 7
