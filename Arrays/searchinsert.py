class Searchinsert:
    def serins(self,nums,target):
        if not nums:
            return 0
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]< target:
                left += 1
            else:
                right -=1
        return left

obj = Searchinsert()
nums = [1,4,5,6,8,9,9,10]

print(obj.serins(nums,7))