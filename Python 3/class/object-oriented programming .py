#object-orriented programming creates more complex ways to track information using "classes"

# classes are similar to a list or a dictionary, but we can customize it to track the exact information we want to use

#blueprint of an object, it specifies specific information but doesnt created anything in the actual program

class Person: #you always need to use init() after this
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
#init must always have a self parameter

#classes are NOT!! objects only a templates, another way to say creating an objext using a class is to say you created an instance of the class

#instances are actual objects created using the class

#its like a forum, the filled out information is the instance but the forum itself is the class

#checkpoint

class Dog: 
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Car:
    def __init__(self, kind, color, year):
        self.kind = kind
        self.color = color
        self.year = year

class Tree:
    def __init__(self, fruit, height, leaf, flower, seed):
        self.fruit = fruit
        self.height = height
        self.leaf = leaf
        self.flower = flower
        self.seed = seed