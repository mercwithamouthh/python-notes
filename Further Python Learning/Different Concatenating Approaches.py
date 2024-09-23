#plus symbol
name = "James"
age = 16
grade = 10

print("Hello my name is " + name + " and I am " + str(age) + " years old and am in grade " + str(grade))

#f-string approach

print(f"Hello my name is {name} and I am {age} years old and am in grade {grade}")

#comma approach

product = "shoes"
price = 10

print("Today we have", product, "on sale for only", price)

#benefits of f-string and comma approaches are able to concatenate without needing to convert integers to string data types

#checkpoint

name = "Caleb"
dogs = 2
location = "AZ"

print("My name is " + name + " and I have " + str(dogs) + "dogs and live in " + location)

print(f"My name is {name} and I have {dogs} dogs and live in {location}")

print("My name is", name, "and I have", dogs, "dogs and live in", location)