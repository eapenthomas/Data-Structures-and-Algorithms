def max_subarray(nums):
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    return max_global

# def max_subarray(nums):
#     max_current = max_global = nums[0]
#     for i in range(1,len(nums)):
#         max_current = max(nums[i],max_current+nums[i])
#         max_global = max(max_current,max_global)
#     return max_global
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    return (x * y) // compute_hcf(x, y)

# Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"HCF: {compute_hcf(a, b)}")
print(f"LCM: {compute_lcm(a, b)}")


l1 =[2,5,1,7,-3,-11,7,-6,-2,4]
print("ms = ",max_subarray(l1))
