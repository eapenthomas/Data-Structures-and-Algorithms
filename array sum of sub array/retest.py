# def merge(arr, low, mid, high):
#     left = arr[low:mid + 1]
#     right = arr[mid + 1:high + 1]
#     i = j = 0
#     k = low
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#     for i in range(i, len(left)):
#         arr[k] = left[i]
#         k += 1
#
#     for j in range(j, len(right)):
#         arr[k] = right[j]
#         k += 1
# def mergesort(arr,low,high):
#     mid = (low+high)//2
#     if low< high:
#         mergesort(arr,low,mid)
#         mergesort(arr,mid+1,high)
#         merge(arr,low,mid,high)
#
# arr = [2,6,4,5,1,9,0]
# mergesort(arr,0,len(arr))
# print("sorted array : ",arr)

# li = [4,6,7,2,1,4,5,6,3,8,9,0,5,4,3]
# target = 10
# for i in range(len(li)):
#     cursum = 0
#     for j in range(i,len(li)):
#         cursum = cursum + li[j]
#         if cursum == target:
#             print(li[i:j+1])

arr = [3,6,5,4,1,2,2,5,7,1,0]
k =3
maxsum = sum(arr[:k])
cursum = maxsum
for i in range(k,len(arr)):
    cursum += arr[i] - arr[i-k]
    maxsum = max(cursum,maxsum)
print(maxsum)
