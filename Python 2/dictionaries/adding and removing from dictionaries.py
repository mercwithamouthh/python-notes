#--Adding

classmates = {
    "Billy": 8,
    "Vance": 15,
    "Alice": 10,
}

classmates["Lily"] = 6

print(classmates)
#you can add to an empty dictionary as well

friends = {}

friends["Lily"] = 6
friends["James"] = 10

print(friends)

#--Removing items
#use the pop method

classmates.pop("Alice")

print(classmates)

#checkpoint

friends["Sebastian"] = 8
friends["Shiloh"] = 10

print(friends)

friends.pop("Shiloh")

print(friends)