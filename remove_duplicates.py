def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


print(remove_duplicates(["1","2","2","3"]))