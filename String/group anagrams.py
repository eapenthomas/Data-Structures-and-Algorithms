from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
        # updating the  position when the letter is found based on ascii
            for c in s:
                count[ord(c) - ord('a')] += 1
        # creating the key for the dictionary
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())

strs =["eat","tea","tan","ate","nat","bat"]
sol =  Solution()
print(sol.groupAnagrams(strs))

# Time : O(n * m)
# space : O(n * m)