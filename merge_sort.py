def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr//2)]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # merged array idx

        