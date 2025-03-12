def majority(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


nums=[2,5,7,2,3,2,2]
print(majority(nums))
