def containsdupli():
    nums = [1, 4, 3, 2, 6,7, 7]
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(containsdupli())


