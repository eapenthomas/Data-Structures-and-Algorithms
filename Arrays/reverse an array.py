def revarray(nums,low,high):
    if low == high:
        return nums
    while low < high:
        nums[low],nums[high] = nums[high],nums[low]
        low += 1
        high -= 1
    return nums
arr = [1,3,5,7,9]
print(f"array = {arr} \n reversed array : {revarray(arr,0,len(arr)-1)}")