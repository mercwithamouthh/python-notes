#fundmental data structures used in computer science

#sata storage technique characterized by a last in, first out strategy AKA when you add data to a stack the most recent addition is the first thing thats returned

#stacks have two main functions - append()/push() and pop()

stack = [1, 2, 3, 4, 5] #looks like a list because lists are a type of stack


#append() how data is added to a stack (push does the same thing)
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

#pop() deletes the very top element of the stack

stack.pop()

print(stack)

stack = []

stack.append('g')
stack.append('o')
stack.append('o')
stack.append('b')

stack.pop()

print(stack)

stack = []

first = "r"

second = "t"

third = "s"

fourth = "y"

fifth = "o"


stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)

print(stack)

answer = ["apples", "steak", "potatoes", "carrots"]

letterS = input("What food should we bring?")

if "s" in letterS:
    answer.append(letterS)
    print(answer)
else:
    print("The input doesn't have the letter s")