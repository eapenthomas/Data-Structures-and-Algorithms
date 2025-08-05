n= 5
res = []
for i in range( n):
    temp = []
    s = str(11**i)
    for j in range(i+1):
        temp.append(s[j])
    res.append(temp)
print(res)




