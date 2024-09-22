# list_1 = ["1", "3", "4", "7", "8"]
# list_2 = ["1", "2", "5", "6", "7"]

# unique_elements = list(set(list_1).symmetric_difference(set(list_2)))
# unique_elements.sort()  # Optional: to sort the result
# print(unique_elements)
# ------------------------------------------------------------------------

# Lists to compare
list_1 = ["1", "3", "4", "7", "8"]
list_2 = ["1", "2", "5", "6", "7"]

# Step 1: Find elements in list_1 that arggggge NOT in list_2
unique_from_list_1 = []
for item in list_1:
    if item not in list_2:  # If the item is NOT in list_2, add it to the result
        unique_from_list_1.append(item)

# Step 2: Find elements in list_2 that are NOT in list_1
unique_from_list_2 = []
for item in list_2:
    if item not in list_1:  # If the item is NOT in list_1, add it to the result
        unique_from_list_2.append(item)

# Step 3: Combine both results to get all unique elements
unique_elements = unique_from_list_1 + unique_from_list_2

# Optional: Sort the result if you want them in order


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
       
        while arr[j-1] > arr[j] and j > 0:
            # print("Found more value!")
            # break
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

insertion_sort(unique_elements)
# Final result
print(unique_elements)
