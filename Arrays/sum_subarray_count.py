from collections import defaultdict
def subarraySum(nums, k):
    result = []
    for i in range(len(nums)):
        cursum = 0
        for j in range(i,len(nums)):
            cursum += nums[j]
            if cursum == k:
                result.append(nums[i:j+1])
    return print(len(result))


def subarraySumcount(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Important: handles subarrays starting at index 0
    count = 0
    cursum = 0
    for num in nums:
        cursum += num
        # Check if there’s a prefix sum that satisfies cursum - k
        if (cursum - k) in prefix_count:
            count += prefix_count[cursum - k]
        # Add current prefix sum to the map
        prefix_count[cursum] += 1
    return print(count)

nums = [1,2,3,2,3,3]
k = 5
subarraySumcount(nums,k)