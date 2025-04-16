def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quicksort(left)+middle+quicksort(right)
arr = [2, 5, 87, 4, 5, 9, 0, 3, 67, 6, 11, 32, 4]
print(quicksort(arr))