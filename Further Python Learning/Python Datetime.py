import datetime #lets you work with dates and times

x = datetime.datetime.now() #exact time (even seconds) from when you press "run"
print(x)

#DATE AS A STRING

#the date isnt a datatype itself so it needs to be converted to a string in order to be used in a program

#  strftime()

#str is string and f is format
#  print(x.strftime(placeholder))

#TODAY
x = datetime.date.today()

print(x)

#LOCAL TIME
#use"%X"
x = datetime.datetime.now()

print(x.strftime("%X"))

#2 DIGIT MONTH
#use "%m"
print(x.strftime("%m"))

#2 DIGIT DAY
#use "%d"
print(x.strftime("%d"))

#4 DIGIT YEAR
#use "%Y"
print(x.strftime("%Y"))

#OTHER

#WEEKDAY SHORT %a EX: Thurs

#WEEKDAY LONG %A EX: Thursday

#MONTH SHORT %b EX: Sept

#MONTH LONG %B EX: September

#2 DIGIT YEAR %y EX: 24

#MINUTE %M EX: 35

#SECOND %S EX: 30

#strftime() converts dates to string and strptime() converts string to date format