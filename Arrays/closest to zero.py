class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = abs(nums[0])
        for i in range(1,len(nums)):
            if abs(nums[i]) < closest:
                closest = nums[i]
        return closest



s = [-1,1,1,2,1]
sol = Solution()
print(sol.findClosestNumber(s))