from collections import  Counter
def containsdupli():
    nums = [1, 4, 3, 2,6, 6, 7]
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            return True
    return False

print(containsdupli())


