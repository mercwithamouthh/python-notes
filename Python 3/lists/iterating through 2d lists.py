my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * 2
print(my_list)
#accessing each item in each list with range()

#first you need to know how many rows and cols there are

#create a loop that moves through the range of rows, each item loops through a range of columns

#checkpoint

rows = 5
cols = 3
my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * 3
print(my_list)

my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

numbers = int(input("Whats your favorite number?"))
rows = 4
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * numbers
print(my_list)

# Get user inputs for the variables
x = int(input("What is the first number? "))
y = int(input("What is the second number? "))
z = int(input("What is the third number? "))

# Define the 2D list with the user inputs
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
rows = 4
cols = 3

largest = 0

for i in range(rows):
    for j in range(cols):
        if my_list[i][j] > largest:
            largest = my_list[i][j]
print(largest)