#a function is a chunck of code that only runs when its is called, this is helpful if you write code but arent ready to use it yet.

#--Functions in python are definded using def as the abbreviation followed by the name by parethesis

def weather():
    print("Its a soggy day outside!")
#code will not print because you have not called the function 

weather()

#--Local and Gloable Scope Variables

#a local variable is when you want to create a variable within a function, they can only be used insde a function

favorite = "I love juice"
def myfunction():
    fruit = "apple"
    print(fruit)

myfunction()

print(favorite)
#variables created outside functions are called global variables, like the variable favorite

#if you want a variable inside a function to be global you can use the global keyword

fav = "i hate juice"
def notmyfunction():
    global veggies 
    veggies = "broccoli"
    print(veggies)
notmyfunction()

print(fav)
print(veggies)

#global allows for veggies to be outside of the function

#checkpoint 

def race():
    print("I won the race")

race()