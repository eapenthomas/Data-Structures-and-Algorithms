a = [1,2,3,4,51,6,7,8,9]
target =7
nums_map = {}
for i,val in enumerate(a):
    compliment = target -val
    if compliment in nums_map:
        print(compliment,val)
    nums_map[val] =i

print('----------------------------------------------')
nums_maps = {}
a = [1,2,3,7,8,0,3,4]
target =5
for j,num in enumerate(a):
    compliments = target - num
    if compliments in nums_maps:
        print(nums_maps[compliments],j)
    nums_maps[num] = j


