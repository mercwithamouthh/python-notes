"23" #string
23 #int
23.0 #float

#if you try to do math with a string ("23" * 4) it would print out wrong (23232323) so in order to do it correctly you need to convert it to an integer

#--Converting to int
age = "16"
age = int("16")
print (age)
#now its an integer
print(age * 2) #gives you 32 instead of 1616

gpa = 3.7
gpa = int(3.7)
print(gpa)
#float becomes int, when becoming an int it does not round down it drops the decimal

#--Converting to string

fries = 30
fries = str(30)
print(fries)
#now its a string

#--Converting to float

pizza = 4
pizza = float(4)
print(pizza)
#now a float