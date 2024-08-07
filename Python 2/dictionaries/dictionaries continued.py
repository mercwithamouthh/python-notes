#--Dcitionary length

classmates = {
    "Billy": 8,
    "Vance": 15,
    "Alice": 10,
    "Lily": 6,
    "Xavier": 12
}

print(len(classmates))

#--Check if key is in dictionary

if "Vance" in classmates:
    print("Vance is in your dictionary")

#can also use not in 

if "Shelby" not in classmates:
    print("Shelby is not in your dictionary")

#--Converting from a list to dictionary

garden = ["pumpkins", "squash", "corn", "tomatoes"]

garden_dictionary = dict.fromkeys(garden, "Harvested")

print(garden_dictionary)

#checkpoint

coins = {
    "pennies": 1,
    "nickels": 2,
    "dimes": 3,
    "quarters": 4
}
print(coins)

coins["silver dollar"] = 5

coins.pop("pennies")

print(coins)
print(len(coins))

#work schedual

work = {
    "monday" : 4,
    "tuesday" : 8,
    "wednesday" : 6,
    "thursday" : 5,
    "friday" : 9
}

work["saturday"] = 7

work.pop("wednesday")

print(len(work))

if "friday" in work:
    print("friday is in work")

#fruit shopping list

shopping = {}

apples_need= int(input("How many apples do you need?"))
bananas_need= int(input("How many bananas do you need?"))
strawberries_need= int(input("How many strawberries do you need?"))

if apples_need > 3:
    apples_buy = apples_need - 5
    shopping["apples"] = apples_buy

if bananas_need > 7:
    bananas_buy= bananas_buy - 7
    shopping["bananas"] = bananas_buy

if strawberries_need > 3:
    strawberries_buy= strawberries_need - 3
    shopping["strawberries"] = strawberries_buy

print(shopping)

