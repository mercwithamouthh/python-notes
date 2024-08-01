#Conditions uses a comparison operator >, >=, <, <=, = (greater than, greater than equal to, less than, less than equal to, and equal to)

#When using the = sign as a conditional you must use two (==) otherwise you are declaring a variable

friend_pet = "poodle"
your_pet = "fish"
if friend_pet == your_pet:
    print("You and your friend have the same pet!")
else:
    print("You and our friend have different pets.")

#if you want to chekc if two values are not equal you have to use !=

if friend_pet != your_pet:
    print("You and our friend have different pets.")
else:
    print("You and your friend have the same pet!")

#you can use and in order to check if two different conditions are true, you dod this by putting and in between conditions

yourpet = "gerbil"
yourneed = "exercise"

if yourpet == "dog" and yourneed == "animal companion":
    print("You are allowed to bring your pet inside the store")
else:
    print("You cannot bring your pet inside the store.")

#if you want to check one or two different conditions then use or, same concept as and

if yourpet == "fish" or yourpet == "reptile":
    print("You are allowed to bring you pet inside the classroom")
else:
    print("You cannot bring you pet inside the classroom")

#checkpoint

age = int(input("How old are you? "))
#changed to an int so the if statement at the end can process it corectly
license_input = input("Do you have your license? (yes or no): ")
#this triggers the boolean
if license_input == "yes":
    license = True
else:
    license = False

if age >= 16 and license:
    print("You are old enough to drive")
else:
    print("You are not able to drive")