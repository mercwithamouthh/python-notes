#python has many libraries with code that already exists, instead of having to write your own code you can use these libraries instead

import math 

#ROUNDING UP

x = math.ceil(3.2) #will round up no matter what
print(x) 

#ROUNDING DOWN

x = math.floor(3.2)
print(x)

#VALUE OF PI

x = math.pi #true value of pi
print(x)

#SQUARE ROOT

x = math.sqrt(100)
print(x)

#MULTIPLY BY A POWER

x = pow(2, 4)
print(x)

#checkpoint

#biking town

people = int(input("How many people are in the town?"))

bikes = int(input("How many bikes are in the town?"))

divided = people / bikes

total = math.ceil(divided)

print("In this town, for every bike that exists there are " + str(total) + " people.")

#cube volume

cube = int(input("Insert a number"))

x = pow(cube, 3)

print(x)