#--Funciton parameters are what goes inside the parentheses of the function declaration

def weather(type):
    print("Its a soggy day outside because it is " + type)

weather("raining")
#can be done multiple times
weather("snowing")
weather("drizzling")

#functions can also have more than one parameter

def gifts(first, second):
    print("Your first choice for a birthday gift would be " + first)
    print("Your second choice for a birthday gift would be " + second)

gifts("bike", "basketball")
gifts("speaker", "tickets")