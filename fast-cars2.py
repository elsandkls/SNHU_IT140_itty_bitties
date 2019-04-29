
# Get our car speeds from the command line
import sys
speed1 = int(sys.argv[1])
speed2 = int(sys.argv[2])

# Write your code below
if speed1 > 70 and speed2 > 70:
  print("2 fast cars")
elif speed1 > 70 or speed2 > 70:
  print("1 fast car")
else:
  print("no fast cars")



