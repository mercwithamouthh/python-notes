#tuples are unchangeable

instruments = ("clarinet", "piano", "drum", "violin")

print(instruments)

#its not obvious but the use of parenthesis shows us this

#you can access specific items
print(instruments[1])

#this will print out piano because indexing starting at 0

#you can do negative indexing that starts counting at -1

print(instruments[-1])

#range of indexing

print(instruments[1:3])

#checking if an item exists

if "piano" in instruments:
    print("the tuple contains the value of piano")
else:
    print("the tuple does not contain the value of piano")

#checkpoint 

grades = (95, 70, 85, 92, 100)

print(grades)

print(grades[-2])

print(grades[0:3])

#check for number

friends = (3, 5, 7, 8, 10, 2, 12, 4)

# Input one number
number = int(input("Enter a number: "))

# Check if the number is in the tuple
if number in friends:
    print("Yes")
else:
    print("No")

#Third from last

# Create a tuple with 8 items
my_tuple = (3, 5, 7, 8, 10, 2, 12, 4)

# Using negative indexing, print out the third to last item in the tuple
print("Third to last item (negative indexing):", my_tuple[-3])

# Using positive indexing, print out the third to last item in the tuple
print("Third to last item (positive indexing):", my_tuple[5])

# Using range, print out the first half of the tuple
print(my_tuple[0:4])
