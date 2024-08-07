#can put any code inside for loop

#the loop moves through a list and checks to see if each item fits the conditional

student_ages = [14, 17, 12, 14, 15, 18, 19, 10]

for x in student_ages:
    if x >= 16:
        print("This student is old enough to drive.")
    else:
        print("This student is not old enough to drive.")
#first indent is responding to the for loop, second indent is responding to the if statement

#range of a list is all the index spots between two numbers

smells = ["skunk", "lilac", "rain", "ocean", "garabge", "cleaner", "cookies"]

print(smells[2:5])

#can also be used to run code a certain number of times 
#ex: for x in range(5): will run 5 times

#loops can update variables with each loop 

my_list = [2, 5, 8, 10]

total = 0

for x in my_list:
    total = total + x

print (total)
#this add the numbers of my_list everytime the loop has run leading to the answer of 25

#checkpoint

foods = ["mushrooms", "broccoli", "fish", "tomatoes"]

for x in foods:
    if x == "mushrooms":
        print( x + " is gross")
    elif x == "broccoli":
        print( x + " is gross")
    elif x == "fish":
        print( x + " is gross")
    else:
        print( x + " is the worst thing ever")
