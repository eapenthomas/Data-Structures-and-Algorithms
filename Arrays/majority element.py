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

nums=[3,3,3,2,3,2,2,2,1,2,2,3]
for i,num in enumerate(nums):
    print(i,num)
