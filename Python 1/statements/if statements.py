#--If statements tells the computer to something is a certain condition occurs, they start with if following a condition and finishing off with a colon

#after the condition the next line of code is indented to signify that this is the code that is executed if the condition is met

#conditions uses a comparison operator >, >=, <, <=, = (greater than, greater than equal to, less than, less than equal to, and equal to)

#examples

Frank_age = 23
Bob_age = 40
if Bob_age > Frank_age:
    print("Bob is older than Frank")
    print("Bob is pretty old")

#the else statement will catch everything that is not included in the If statement

Janet_age = 16
Eva_age = 5
if Eva_age > Janet_age:
    print("Eva is older than Janet")
else:
    print("Eva is younger")

if Eva_age == Janet_age:
    print("Eva and Janet are the same age!")
else:
    print("They are different ages")