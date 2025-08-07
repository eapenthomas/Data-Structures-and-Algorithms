from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # top - down dp tabulation method
        dp = [1] * n
        maxp = dp[0]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return print (max(dp))

sol = Solution()
nums =[10,9,2,5,3,7,101,18]
num1 =[0,1,0,3,2,3]
sol.lengthOfLIS(num1)
sol.lengthOfLIS(nums)
