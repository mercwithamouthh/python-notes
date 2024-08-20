#searches the list for the smallest value and placing it at the beginning of the list, when it does this it creates a sorted and unsorted list

#pseudocode for selection sort

function SelectionSort(list)

    for all elements (i) in list:
        minimum = i
        for remaining elements (j) in list:
            if list[j] < list[minimum]
                minimum = j
            end if
        end for
        if the index of minimum != i
            swap list[minimum] an list[i]
        end if
    end for
    return list
end SelectionSort

#much faster than bubble sort

#checkpoint

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

num = int(input("insert a number into the list"))

arr.append(num)

for i in range(len(arr)):
    # Assume the current element is the smallest
    smallest_index = i
    # Check the rest of the array to find if there is a smaller element
    for j in range(i + 1, len(arr)):
        if arr[smallest_index] > arr[j]:
            smallest_index = j
    # Swap the found smallest element with the current element
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
print(arr)