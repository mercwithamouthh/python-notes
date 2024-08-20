#takes the next unsorted value and inserts it into the correct place in the sorted list

function InsertionSort(list)

   insert_spot = 0
   val_to_insert = 0

   for all elements (i) in list:
      val_to_insert = list[i]
      insert_spot = i

      while insert_spot > 0 and list[insert_spot-1] > val_to_insert:
         list[insert_spot] = list[insert_spot - 1]
         insert_spot = insert_spot - 1
      end while

      list[insert_spot] = val_to_insert

   end for
   return list
end InsertionSort

#checkpoint

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

num = int(input("Insert a number into the list: "))

arr.append(num)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = key

print(arr)