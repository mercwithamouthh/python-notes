#sort lists into numerical order comparing two adjacent numbers and switching their order if necessary 

#only works with numbers

#--PSEUDOCODE

#pseudocode is a way to wrtie out the concept of a program that isnt language specific, looks like computer code but written in  more readable way

#pseudocode for bubble sort

function BubbleSort(list)

    for all elements in list:
        if list[i] > list[i+1]
            swap(list[i], list[i+1])
        end if
    end for 
    return list
end BubbleSort

#bubble sort is very inefficient and other sorting algorithms are better.

#checkpoint

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

num = int(input("Pick a number: "))

arr.append(num)

def bubbleSort(sort_list):
    n = len(sort_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]

# Call the bubbleSort function with the updated list
bubbleSort(arr)

# Print the sorted list
print(arr)