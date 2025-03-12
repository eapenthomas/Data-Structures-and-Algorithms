def mergesort(arr, low, high):
    if low < high:  # Base case: Stop when the subarray has one element
        mid = (low + high) // 2  # Calculate the middle index
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    for i in range(i,len(left)):
       arr[k] =left[i]
       k +=1

    for j in range(j,len(right)):
        arr[k] = right[j]
        k +=1


arr = [7, 5, 8, 3, 4, 9, 2]
mergesort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
