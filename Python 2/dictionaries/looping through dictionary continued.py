#can combine with if statements

classmates = {
    "billy" : 8,
    "vance" : 12,
    "alice" : 10,
    "eliza" : 15,
    "xavier" : 6
}

for x in classmates:
    if x == "eliza":
        print("This person wants to be anonymous")
    else:
        print(x)

#can use loops to create dictionaries

period = int(input("how many class periods do you have?"))
schedule = {}
for i in range(period):
    subject = input("what subject?")
    num_people = input("how many people are in your " + subject + " class?")
    if subject not in schedule:
        schedule[subject] = num_people
print(schedule)

#checkpoint

ride = {
    "bob": 5,
    "kevin": 8,
    "stuart": 7,
    "jeffy": 4,
    "jimmy": 9,
}

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride")
    else:
        print("This person is too short to ride")

#check for a key

dictionary = {
    7: "first",
    3: "second",
    4: "third",
    8: "fourth",
    9: "fifth",
}

my_list = [int(n) for n in input("Enter a list of integers separated by spaces: ").split()]

# Check if each integer in the list is a key in the dictionary
for number in my_list:
    if number in dictionary:
        print("Yes")
    else:
        print("No")

#power dictionary

# Input the number of keys in the dictionary
n = int(input("How many keys in your dictionary? "))

# Initialize an empty dictionary
my_dict = {}

# Generate the dictionary with keys from 0 to n and values as the square of the keys
for n in range(n):
    my_dict[n] = n * n

# Print the dictionary
print(my_dict)
