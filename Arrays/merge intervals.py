arr1 = [[1,3],[2,6],[8,10],[11,15]]
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval:interval[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0],max(merged[-1][1],interval[1])]
        return merged

sol = Solution()
print(sol.merge(arr1))
