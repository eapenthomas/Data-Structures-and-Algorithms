str1 = "boy good is eapen"
arr = []
temp =""
arr1 =[]
for c in str1:
    if c == ' ':
        arr1.append(temp)
        temp = ""
    else:
        temp +=c
arr1.append(temp)
print(arr1)
l,h = 0, len(arr)-1
while l<h:
    temp = arr1[l]
    arr1[l] =arr1[h]
    arr1[h] = temp
    l +=1
    h -=1
result = " ".join(arr1)
print(result)
