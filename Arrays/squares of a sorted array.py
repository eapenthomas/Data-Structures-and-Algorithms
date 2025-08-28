class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums)-1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        return result[::-1]

sol = Solution()
print(sol.sortedSquares([-5,-2,0,1,2,3,4]))