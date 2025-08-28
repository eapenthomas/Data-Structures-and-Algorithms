str1 = "boy good is eapen"
arr = []
temp =""
arr1 =[]
arr = str1.split(" ")
print(arr)
l,h = 0, len(arr1)-1
while l<h:
    temp = arr1[l]
    arr1[l] =arr1[h]
    arr1[h] = temp
    l +=1
    h -=1
result = " ".join(arr1)
print(result)
