def maxsub(nums):
    cursum = 0
    maxsum = 0
    for i in range(len(nums)):
        cursum = max(nums[i],cursum+nums[i])
        maxsum = max(cursum,maxsum)
    return print(maxsum)

nums = [1,5,-3,-7,5,7,-2,5]
maxsub(nums)