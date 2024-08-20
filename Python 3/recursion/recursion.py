#a way to simplify programs, however its an abstract concept and takes beginners time to understand

#recursion is writing functions that call themselves

#point is to break up lists into smaller chuncks to work with

houses = ["ahmeds house", "clarks house", "xin lis house", "melissas house"]

#each function call represents an elf doing his work
def diliver_presents_recursively(houses):
    #worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("dilvering presents to " + house)
    else: #manager elf doing his work
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        diliver_presents_recursively(first_half)
        diliver_presents_recursively(second_half)
diliver_presents_recursively(houses)
#divides his work among two elves

#checkpoint

this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala'] 

def feeding(this_list):
    if len(this_list) == 1:
        animals = this_list[0]
        print("The " + animals + " has been fed")
    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]

        feeding(first_half)
        feeding(second_half)
feeding(this_list)

books = [int(n) for n in input("Input a list of numbers").split()]

def pairs(books):
    if len(books) == 2:
        total_length = books[0] + books[1]
        print(total_length)
    else:
        mid = len(books) // 2
        first_half = books[:mid]
        second_half = books[mid:]

        pairs(first_half)
        pairs(second_half)
pairs(books)

flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

def orchard(flowers):
    if len(flowers) == 1:
        pollinated = flowers[0] * 3
        print(pollinated)
    else:
        mid = len(flowers) // 2
        first_half = flowers[:mid]
        second_half = flowers[mid:]

        orchard(first_half)
        orchard(second_half)
orchard(flowers)