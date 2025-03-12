a = [1,2,3,4,51,6,7,8,9]
target = 7
res = []
# for i in range(len(a)-1):
#     cursum = 0
#     for j in range(i+1,len(a)):
#         if a[i] + a[j] == target:
#             res.append((a[i],a[j]))
# print(res)

start = 0
cursum = 0
for end in range(len(a)):
    cursum = cursum + a[end]
    while cursum > target and start <= end:
        cursum = cursum - a[start]
        start = start +1
    if cursum == target:
        res.append((a[start:end+1]))
print(res)