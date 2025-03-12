from collections import Counter
nums =[2,5,8,9,4,1]
target =7
nums_map ={1:"key",2:"value"}
print(nums_map)


# n =8
# print(bin(n).replace("0b",""))
# binary = ""
# while n > 0:
#     binary += str(n%2)
#     n = n//2
# k =(binary[::-1])
#
# dec = int(k,2)
# print(dec)

n = "apple4"
s= Counter(n)
char,counts = s.most_common(1)[0]
print("char = ",char," count = ",counts)