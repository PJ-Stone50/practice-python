list_1 = ["1","3","4","7","8"]
list_2 = ["1","2","5","6","7"]

duplicates = [item for item in list_1 if  item in list_2]

print(duplicates)