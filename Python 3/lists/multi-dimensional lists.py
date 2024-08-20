#one dimensional list 

n = 5 
list = []
for i in range(n):
    list.append(0)
print(list)

#two dimensional list

rows = [1, 2, 3]
cols = ["red", "orange", "yellow", "green"]
list = []
for i in rows:
    col = []
    for j in cols: 
        col.append(j)
    list.append(col)
print(list)

#using range to create 2d lists

rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(i)
    list.append(col)
print(list)

#checkpoint

rows = 5
cols = 3
list = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(5)
    list.append(row)
print(list)

names = ["caleb", "logan", "wade", "james"]
last = ["smith", "gomez", "miller", "wright"]
list = []

for i in names:
    name = []
    for j in last:
        name.append(i + " " + j)
    list.append(name)
print(list)

fruit = input("name some fruit!").split()
flavors = ["apple", "grape", "peach", "cinnamon", "vanilla"]
combo = []
for i in fruit:
    fruits = []
    for j in flavors:
        fruits.append(i + " " + j)
    combo.append(fruits)
print(combo)
