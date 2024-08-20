#python can open files as long as you give it its exact location, it can read it edit them ect

#this can be useful in many ways 

#we use text files because they dont take up much space

#reading files

file = open("example.txt", "r")
#r is the mode that can read, it cannot edit anything the program can only read it

print(file.read())
#prints the text of the file to read

file.close
#its important to close files to free up space

#checkpoint

file = open("speech.txt", "r")
print(file.read())