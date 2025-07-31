from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # converting to negation values to make it a max heap
        for i in range(n):
            nums[i] = -nums[i]
        # creating a max heap
        heapq.heapify(nums)
        # poping upto k-1 th element
        for _ in range(k-1):
            heapq.heappop(nums)
        # poping the kth largest value and return its negated figure
        return print(-heapq.heappop(nums))

nums =[3,2,1,5,6,4]
k =2
sol = Solution()
sol.findKthLargest(nums,k)