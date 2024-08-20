#there are 2 ways to edit a file in python, one of them being to append text to the file

#when opening files weve used r to read them a is to go into append mode, you can also use the w command to write which completely deletes the old text and replaces it with new text

file = open("example.txt", "a")

file.write("I love programming!")

file.close()

#check to see if it worked

file = open("example.txt", "r")
print(file.read())

#checkpoint

file = open ("letter.txt", "a")
file.write("From your Pen Pal")
file.close()

file = open("letter.txt", "r")
print(file.read())

file = open("report.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("report.txt", "r")
print(file.read())