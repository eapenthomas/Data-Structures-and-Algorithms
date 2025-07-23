from itertools import permutations
# s = [5,3,2,5,8,1,1,3,1,0,3,5,7]
# target =8
# for i in range(len(s)):
#     cursum = 0
#     for j in range(i,len(s)):
#        cursum = cursum+s[j]
#        if cursum == target:
#            print(s[i:j+1])


# s = [5, 3, 5, 8, 1, 1, 3, 1, 0, 3, 5, 7]
# target = 8
# res = []
# for i in range(len(s)):
#     cursum = 0
#     for j in range(i,len(s)):
#         cursum += s[j]
#         if cursum == target:
#             res.append(s[i:j+1])
# print(res)


s = [5, 3, 5, 8, 1, 1, 3, -1, 0, 3, 5, 7]
target =7
start = 0
cursum = 0
res = []
for end in range(len(s)):
    cursum = cursum + s[end]
    while cursum > target and start <= end:
        cursum = cursum - s[start]
        start += 1
    if cursum == target:
        res.append(s[start:end + 1])
print(res)


