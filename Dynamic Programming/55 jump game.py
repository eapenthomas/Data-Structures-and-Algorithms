from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Aproach : end to start
        # Time  O(n)
        # space O(1)
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            maxjump = nums[i]
            if i+maxjump >= target:
                target = i
        return target == 0

sol = Solution()
nums =[2,3,1,1,4]
nums1 =[3,2,1,0,4]
print(sol.canJump(nums))
print(sol.canJump(nums1))