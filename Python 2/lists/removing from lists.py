#you can remove things from lists using remove()

goats = ["billy", "frannie", "leslie", "barbara", "scott"]

print(goats)

goats.remove("frannie")

print(goats)

#if there are multipule elements with the same name in a list the remove method will take out the first one that matches

goats.append("bob")
goats.insert(2, "bob")

print(goats)

goats.remove("bob")

print(goats)

#if you want to remove an item from a list but not remove the value use pop()

favorite = goats.pop(3)

print(favorite + " is my favorite goat")

print(goats)

#checkpoint

harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]

harvest.remove("squash")

harvest.pop(1)

print(harvest)