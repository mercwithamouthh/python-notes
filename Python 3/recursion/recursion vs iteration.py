#basically iteration is the long way and recursion is the easier way

#iterative factorial 

def iterative_factorial(n):
    result = 1 
    for i in range(1, n + 1):
        result *= i
    return result 

print(iterative_factorial)

#recursive factorial

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))

print(factorial(4))

#checkpoint

n = int(input("Insert a number: "))

def function(n):
    if n <= 1:
        return 1
    else:
        return n * (function(n-1))

print(function(n))
    
list_of_nums = [int(n) for n in input("Insert some numbers").split()]

def function(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + function(nums[1:])

print(function(list_of_nums))

sequence = int(input("Insert a number"))

def fibonacci_sequence(n, sequence=None):
    if sequence is None:
        sequence = []

    if n == 0:
        return sequence
    elif len(sequence) < 2:
        sequence.append(len(sequence))  # Append 0 for the first element, 1 for the second
    else:
        sequence.append(sequence[-1] + sequence[-2])

    return fibonacci_sequence(n-1, sequence)

print(fibonacci_sequence(sequence))