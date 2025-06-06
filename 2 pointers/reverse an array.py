def reversearray(arr):
    left = 0
    right = len(arr)-1
    while left <right:
        arr[left],arr[right]=arr[right],arr[left]
        left +=1
        right -=1
    return arr

arr = [2,3,4,5,6,7,8,9]
print(reversearray(arr))

# Efficient (O(n) time, O(1) space)