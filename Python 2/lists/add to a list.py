# several ways to add to lists, one being append()

goats = ["billy", "frannie", "leslie", "barbara", "scott"]

goats.append("molly")

print(goats)

#can combine lists using extend()

goats.extend(["janie", "boulder", "penelope", "frank"])

print(goats)

#when you try to extend just a string it will separate every letter
#ex
#---goats.extend("curly")

#---print(goats)

#if you want to add an item to a specific place use insert()

goats.insert(2, "curly")

print(goats)

#checkpoint

flowers = ["rose", "tulip", "lilac", "sunflower"]

flowers.append("lily")

flowers.extend(["daisy", "violet", "hydrangea"])

flowers.insert(3, "lotus")

print(flowers)