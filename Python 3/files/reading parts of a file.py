#read() function allows you to read only parts of the file, by default it will read the whole file but adding a number it will read that many characters from the file

#this will read the whole file
file = open("example.txt", "r")
print(file.read())

file = open("example.txt", "r")
print(file.read(5))
#this prints out 5 characters, this is not indexing which starts at 0

#readline() will read entire lines of a text file

file = open("example.txt", "r")
print(file.readline())
#this will read out the first line of the file

print(file.readline())
print(file.readline())
#this will print out the first 2 lines of the file

#to return all lines in a file use readlines instead of readline

file = open("example.txt", "r")
print(file.readlines())
#this will print out all lines to a file

#when closing a program make sure to close out of the file to save space

file.close()

#checkpoint 

file = open("example.txt", "r")
print(file.read(10))

print(file.readline())
print(file.readline())

file.close()

#read a specific number of characters

number = int(input("How many characters do you want to print?"))
file = open("example.txt", "r")

print(file.read(number))

file.close()

#how many words?

file = open("example.txt", r)
data = file.read()
words = data.split()

print(len(words))

file.close()