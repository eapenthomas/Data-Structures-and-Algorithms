import heapq
def heapsort(arr): # O(n log n)
    n = len(arr)
    newlist =[0]*n
    heapq.heapify(arr)
    for i in range(n):
        minn = heapq.heappop(arr)
        newlist[i] =minn
    return newlist

#constructing max heap
arr = [4,5,7,9,2,1,3,8]
for i in range(len(arr)):
    arr[i]= -arr[i]
print(heapsort(arr))
