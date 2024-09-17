mylist =  ["1","2","3","4","5"]
mylist1 =  [6,-21,25,7,4]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
       
        while arr[j-1] > arr[j] and j > 0:
            # print("Found more value!")
            # break
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

print(mylist1)
insertion_sort(mylist1)
print(mylist1)