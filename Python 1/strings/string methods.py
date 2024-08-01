#--The lower and upper method cause the string to either be uppercase or lowercase

string1 = "HAbabaLOO!!"
print(string1.lower())
print(string1.upper())

#--The replaces method replaces a specified character within the string, putting something inside the parentheses is necessary

string2 = "I am going to turn 16."
print(string2.replace("16","17"))

#--The strip method will remove any white space at the beginning or ending of a string

string3 = " sharks "
print(string3.strip())
#example of the outcome without it
stringex = " sharks "
print(stringex)

#--Indexing gives you the index number of any given character in a string using brakets, this includes spaces (starting at 0)

string4 = "This is an example"
print(string4[5])

#--Slicing uses indexs to print specific slices of a string, in order to do this use a colon in the brackets (This excludes the last index!!!) 

string5 = "This is another example"
print(string5[3:9])

stringevarient = "This is another example of the previous example"
print(stringevarient[2:12:2])

stringvarr = "Can you believe another string varient of the previous one?"
print(stringvarr[:6])

#--Reverse method, start slicing at the end of the string and work backwards, Moving back through the string with a negative number in the third number slot will pull out each letter in turn from back to front.

string6 = "yodel"
reverse = string6[len(string6)::-1]
print(reverse)

#--Split method

string7 = "everything is awesome"
print(string7.split())

#--Length of a string counts the characters starting at 1

print(len(string7))

#--Finding a character in a string will give you were said character is, this will give you the index value meaning you start from 0

print(string7.find("e"))
#this gives you the first instance of said character
print(string7.rfind("e"))
#this gives you the last instance of said character

