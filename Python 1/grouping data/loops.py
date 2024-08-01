#--Loops are used for adressing each piece of data in a sequence (a list, dictionary, or tuple)

desserts = ["cake", "ice cream", "pie", "brownies"]

for x in desserts:
    print(x)

#x is the variable that represents each item on the list, other letters or words can be used

#for statement

#you can execute a variety of code inside the loop

for x in desserts:
    print("I love to eat " + x)

#you can do math inside a for loop

allowance = [ 8, 5, 10, 4, 7]

for x in allowance:
    print(x + 10)

#for loops can be useful with the range command

for x in range(2, 10):
    print(x)

#will print out every number in between the two numbers except the second one (10 in this case) in order to include it add a +1 at the end of the second variable

for x in range(2, 10 + 1):
    print(x)

#you can update variables in a for loop

total = 0

for x in range(4):
    total = total + x

print(total)

#this code loops 4 times, the output is 6 because x gets added to the total, x starts out at 1 first loop and 2 by the second loop ex ex


#checkpoint 

animals = ["hedgehog", "sea urchin", "porcupine", "echidnas"]

for x in animals:
    print(x + "is the spikiest animal ever!")