from functools import cache
def quick_sort(arr):
   if len(arr)< 1:
       return arr
   mid = arr[0]
   left = [x for x in arr if x < mid]
   middle = [x for x in arr if x == mid]
   right = [x for x in arr if x  > mid]
   return quick_sort(left)+middle+quick_sort(right)
# Example usage:
def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
def insertinsort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] > arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] <arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr=[3,114,54,23,7,89,65,98,50,245,78,90,56]
print("Unsorted  : ",arr)
print("bubble    : ",bubble_sort(arr))
print("Quick     : ",quick_sort(arr))
print("selection : ",selection_sort(arr))
print("insertion : ",insertinsort(arr))

