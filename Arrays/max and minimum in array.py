def findminmax(arr):
    n = len(arr)
    if n % 2 == 0:
        if arr[0] < arr[1]:
            small,big = arr[0],arr[1]
        else:
            small,big =arr[1],arr[0]
        i =2
    else:
        small = big =arr[0]
        i =1
    while i<n:
        if arr[i]<arr[i+1]:
            if arr[i]<small:
                small = arr[i]
            if arr[i+1]>big:
                big =arr[i]
        else:
            if arr[i+1]<small:
                small = arr[i+1]
            if arr[i]>big:
                big= arr[i]
        i += 2
    return print(f"small : {small} , big = {big}")
arr = [2,5,4,8,9,6]
findminmax(arr)