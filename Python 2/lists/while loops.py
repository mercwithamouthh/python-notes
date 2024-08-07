#similar to an if statement that repeats over and over while a condition is true

people_in_line = 20

while people_in_line > 0:
    print("There are " + str(people_in_line) + " people in line. Keep the coaster running!")
    people_in_line = people_in_line - 1

#you must include a way for the condition to stop beeing met or else it will continue infinitely 

#this is done with increments or decrements, if one if not included the loop cannot stop

#--Decrement Operator

#some ways to write a decrement operator is 
#people_in_line = people_in_line - 1 or people_in_line -= 1

#this will cause the variable to become a smaller and smaller interger until is reaches 0

#--Increment Operator

#works the same way except it adds
#people_in_line = people_in_line + 1 or people_in_line += 1


#checkpoint 

number = 1

while number <= 50:
    print(number)
    number += 1
