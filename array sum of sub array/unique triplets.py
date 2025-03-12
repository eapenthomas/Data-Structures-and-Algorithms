# arr = [2,-2,0,-1,3,1,1]
# arr.sort()
# result = set()
# print(arr)
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             sum = arr[i]+arr[j]+arr[k]
#             if sum == 0:
#                result.add(( arr[i],arr[j],arr[k]))
# ar1 = list(result)
# print(ar1)


arr = [2,-2,0,-1,3,1,0,0,1] #[-2,-1,0,0,0,1,1,2]
arr.sort()
result= []
for i in range(len(arr)):
    if i>0 and arr[i]==arr[i-1]:
        continue
    left,right = i+1,len(arr)-1
    while left<right:
        cursum= arr[left]+arr[right]+arr[i]
        if cursum == 0:
            result.append([arr[i],arr[left],arr[right]])
            left +=1
            right -=1
            while left<right and arr[left]==arr[left-1]:
                left +=1
            while left<right and arr[right]==arr[right+1]:
                right -=1
        elif cursum <0 :
            left+=1
        else:
            right -=1

print(result)

