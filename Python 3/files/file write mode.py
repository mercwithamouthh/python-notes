#replaces everything in the file with everything new you write

file = open("example.txt", "w")
file.write("This line replaces everything in this file!")
file.close()

#write and append mode can be used to create new text files, if there is no text file with the name it will create a new one

file = open("new_document.txt", "w")

#checkpoint

file = open("example.txt", "w")
file.write("In short, I love to code!")
file.close()
file = open("porcupine.txt", "w")

file = open("ex.txt", "w")
file.write("Never mind")
file.close()

answer = input("what is the answer")
file = open("blah.txt", "w")
file.write(answer)
file.close()
file = open("blah.txt", "r")
print(file.read())