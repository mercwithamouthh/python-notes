#can add an attribute to an object
class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = People("Jasmine", "15", "Femalie")

person.height = "5'6"

print(person.height)

#can remove attributes

#delattr(name) will error
#print(person.name) will error 

#can modify object properties

person.gender = "Male"

print(person.gender)

#can delete things

del person.age
#print(person.age) will error

#can add functions to our classes called object methods

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def greeting(self):
        print("Good Morning")

pet = Dog("Jasmine", "15", "female")

pet.greeting()

#checkpoint

class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather
    def tuesday(self):
        print("We will be hiking on Tuesday")

summer = Vacation( "Hawaii", 2000,"Sunny")

summer.rating = 10

summer.weather = "rainy"

print(summer)

print(summer.rating)

print(summer.weather)

class Friday:
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")

thisWeekend = Friday("Movie", "Charlotte")

thisWeekend.money = 20

thisWeekend.friend = "Shane"

print(thisWeekend)

print(thisWeekend.money)

print(thisWeekend.friend)

class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []
    def spending(self, cost):
        self.total.append(cost)

sportStore = Shopping("Kayak", "High Quality")

sportStore.spending(10)

sportStore.spending(38)

sportStore.spending(24)

print(sportStore.total)



