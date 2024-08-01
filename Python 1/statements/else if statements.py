#You can combine multiple IF statements. When checking for more than one condition you can add an else if statement which should be shortened down to elif

price = 10
your_cash = 8

if your_cash > price:
    print("You have MORE than enough money to buy it.")
elif your_cash == price:
    print("You hve exactly enough money to buy it.")
else:
    print("You do not have enough money to buy it.")

vacation = "mountains"
#can use elif multiple times for a more specific program 
if vacation == "beach":
    print("You love the ocean")
elif vacation == "amusement_park":
    print("You love to ride roller coasters")
elif vacation == "mountains":
    print("You love to get up and away")
else:
    print("You like unique vacation destinations")

#checkpoint

coins = 10

if coins > 20:
    print("You have more than enough money to buy a puppy")
elif coins == 20:
    print("You have exactly enough to buy a puppy")
else:
    print("You do not have enough money to buy a puppy")