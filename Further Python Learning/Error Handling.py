#try block: tests a code for errors

#except block: code to run if an error happens

#else block: code to run if no error happens

#finally block: code to run regardless of the try/except blocks

try:
    print(greeting) #without the try block the code would crash because there is no variable names greeting
except:
    print("a problem occurred")

#else block added, will run cause theres no error
greeting = "hello"

try:
    print(greeting)
except:
    print("a problem occurred")
else: #else block MUST come right after except block
    print("the code worked without a problem")

greeting = "hello"

#adding finally block
try:
    print(greeting)
except:
    print("a problem occurred")
else: 
    print("the code worked without a problem")
finally:
    print("you exception handling is complete") #the finally block is optional

#error handling separates code down into chunks in order to narrow down where bugs are, where otherwise it may be difficult