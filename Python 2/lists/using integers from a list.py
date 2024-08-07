#can be used for math

puppies = [2 ,3 ,6 ,5 ,10]

print(puppies[1] + 10)

#can round values with round() method

pies = 10

shared = pies/3

print(round(shared, 2))
#the number two determines how many decimal points to include in the rounded value

#can find the range of an integer like this

for x in range(0,5):
    print(x)
#will exclude last number (5)

#step

smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "new car", "sweaty feet", "peach"]

print(smells[0:8:2])
#the 2 represents the step, skipping over 2 up until 8 (last number is still not included which would be 8)

for x in range(0, 20, 3):
    print(x)
#another example

#max and min can be found by max() and min()

largest = max(4, 20, 62, 18, 9, 45)
print(largest)

smallest = min(4, 20, 62, 18, 9, 45)
print(smallest)

#checkpoint

lasers = [3, 10, 4, 15, 11]

print(lasers[2] * 10)

print(round(3.14159265, 3))

for x in range(0,10):
    print(x)

for x in range (0,10,2):
    print(x)
