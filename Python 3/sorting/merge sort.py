#divides the list into n sublists where each sublist contains an element from the main list, they are considered sorted because theres only one element in size

#once the sublists are created they get merged until only one list remains which will be sorted

#merge sort is a recursive algorithm so it calls itself when needed

#merge sort needs two functions, a function that divdes the sublists and a function that merges them back together

#pseudocode 

answer = int(input("Enter a number 0 - 100:"))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

arr.append(answer)

def mergeSort(sort_list):
    if len(sort_list) > 1:

        mid = len(short_list)//2
        L = short_list[:mid]
        R = short_list[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_list[k] = L[i]
                i += 1
            else:
                sort_list[k] = R[j]
                j += 1
            k += 1
        
        while j < len(R):
            sort_list[k] = R[j]
            j += 1
            k += 1

mergeSort(arr)
print(arr)

#fastest way to sort

#checkpoint

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

num = int(input("Insert a number: "))
arr.append(num)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Merging the remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Calling the function with the correct name
mergeSort(arr)
print(arr)