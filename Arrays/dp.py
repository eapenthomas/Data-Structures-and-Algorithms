def fact(nums):
    s = []
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                target = nums[i]+nums[j]+nums[k]
                if target == 5:
                    s.append([nums[i],nums[j],nums[k]])
    return s



print(fact([1,2,3,4,-7,-8,-1,0]))