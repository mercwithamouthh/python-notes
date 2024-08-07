#dicionaries are another way to group information similar to lists and tuples

#--Dictionaries are ordered changable and indexed

classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10
}

print(classmates)
#this will print out with them being in a pair the first item in the pairing is called a key and the second item is called a value

names = {
    "person1": "George",
    "person2": "Brenda",
    "person3": "Larry",
    "person4": "Aaliyah",
}

print(names)

#--Accessing Items in the Dictionary

print(classmates["Vance"])
#this prints out 12, it accessed the value paired with the key names Vance

#--Changing Values in the Dictionary

classmates["ALice"] = 15

print(classmates)
#this now prints alices age as 15 instead of 10

#checkpoint 

mountains = {
    "Timpangos": 2,
    "Everest": 4,
    "Kilimanjaro": 3, 
    "Vesuvius": 1,
}

print(mountains)
print(mountains["Vesuvius"])
 
mountains["Kilimanjaro"] = 5
print(mountains)