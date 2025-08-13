def find_min_max(arr,low,high):
    if low == high:
        return arr[low],arr[low]
    if low == high + 1:
        return min(arr[low],arr[high]),max(arr[low],arr[high])
    mid = (low+high)//2
    min1,max1 = find_min_max(arr,low,mid)
    min2,max2 = find_min_max(arr,mid+1,high)
    return min(min1,min2),max(max1,max2)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(log n) (due to recursion stack)
arr = [3,3,4,6,9,-2,11]
minv,maxv = find_min_max(arr,0,len(arr)-1)
print(f"Minimum ={minv} and maximum = {maxv} ")