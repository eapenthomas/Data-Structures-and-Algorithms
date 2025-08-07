def prodself(nums):
    answer= []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod = prod * nums[j]
        answer.append(prod)
    return print(answer)

def productExceptSelf(nums):
    n = len(nums)
    answer = [1]*n
    prefix = suffix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *=nums[i]
    for i in range(n-1,-1,-1):
        answer[i] *= suffix
        suffix *= nums[i]
    return print(answer)

nums = [1,2,3]
print(nums)
productExceptSelf(nums)
prodself(nums)