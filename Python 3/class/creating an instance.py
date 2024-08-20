class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("Jasmine", "15", "Female")
print(p1)

#this only prints out a referance to that object, this will print out an attribute of an object

print(p1.name)
#or you can concatenate different parts
print("Person 1: " + p1.name + " " + p1.age + " " + p1.gender)

#you can create multiple objects from the same class

p2 = Person("George", "67", "Male")

print("Person 2: " + p2.name + " " + p2.age + " " + p2.gender)

#very easy to access information now

#checkpoint

class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material

myObject = Hat("tophat", "black", "silk")

class Fruit:
   
   def __init__(self, shape, kind, size):
         self.shape = shape
         self.kind = kind
         self.size = size

strawberry = Fruit("triangle", "sweet", "small")
pineapple = Fruit("oval", "sweet and sour", "big")
banana = Fruit("crecent", "sweet", "medium")
mango = Fruit("circle", "sweet", "medium")

print(strawberry.kind)
print(pineapple.kind)
print(banana.kind)
print(mango.kind)

class Pet:
   
   def __init__(self, name, kind, age):
         self.name = name
         self.kind = kind
         self.age = age

cat = Pet("eddie", "cat", "5")
dog = Pet("bruce", "dog", "7")
bunny = Pet("judith", "rabbit", "2")

