def majority(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    return  candidate

nums  =[3,3,3,2,3,2,2,2,1]
nums1 =[1,2,3,4,5,6,7,8,9]
for i,num in zip(nums,nums1):
    print(i+num)
