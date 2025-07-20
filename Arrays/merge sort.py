def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    m = n//2
    left = arr[:m]
    right = arr[m:]
    left = mergesort(left)
    right = mergesort(right)
    sortedarray = [0]*n
    lindex = len(left)
    rindex = len(right)
    l = r = i = 0
    while l<lindex and r < rindex:
        if left[l] < right[r]:
            sortedarray[i] = left[l]
            l +=1
        else:
            sortedarray[i] = right[r]
            r += 1
        i += 1
    while l < lindex:
        sortedarray[i] = left[l]
        i +=1
        l += 1
    while r < rindex:
        sortedarray[i] = right[r]
        i +=1
        r += 1

    return sortedarray


arr = [7, 5, 8,0,4, 3, 4, 9, 2]

print("Sorted array:", mergesort(arr))
