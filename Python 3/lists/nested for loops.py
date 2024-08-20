#when you use a for loop inside of another for loop

#1d list
n = 5
list = []
for i in range(n):
    list.append(i)
print(list)

#2d list

rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(j)
    list.append(col)
print(list)

#python lets you write for loops in one line of code

list = ["hello" for i in range(5)]
print(list)

#checkpoint

rows = 3
pets = ["cat", "dog", "hamster", "fish", "rabbit"]
list = [[pet for pet in pets] for _ in range(rows)]
print(list)

mylist = [1, 2, 3, 4, 5]

rows = int(input("how many rows do you want?"))

list = [[num * rows for num in mylist] for _ in range(rows)]
print(list)

rows = input("Input a list of weather ").split()
cols = ["windy", "breezy", "calm"]
weather_wind_combinations = [[f"{weather} {col}" for col in cols] for weather in rows]

print(weather_wind_combinations)