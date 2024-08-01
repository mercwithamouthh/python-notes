#--Concatenating (connecting) Strings

string1 = "i love"
string2 = "batman"
string3 = string1 + string2

print(string3)

string4 = string1 + " " + string2 

print(string4)

#if you want to concatenate a string with an integer do this

age = 16 

print("I am " + str(age) + " years old")

#concatenating numbers is different because the + sign is used as a concatenation symbol and an addition symbol

#--Format Method allows you to combine different variable types with strings

string5 = "Ive ran {} miles today"
miles = 21
print(string5.format(miles))

#you can use multipule integers with the format method using a comma

string6 = "Whats {} plus {}?"
nine = 9
ten = 10
print(string6.format(nine, ten))

#Format by Index
string7 = "Whats {1} plus {0}?"
nine= 9
ten= 10
print(string7.format(ten, nine))

string8 = "The total number of miles we hiked is {1}. We saw {0} deer"
miles = 21
animals = 20
print(string8.format(animals, miles))