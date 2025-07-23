class Remdupli:
    def remove_duplicates(self,nums):
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums [i] = nums[j]
        return nums[:i+1]


red= Remdupli()
nums=[0,0,1,2,3,3,4,5,5,6]
print(red.remove_duplicates(nums))