from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        # letters nte count kittan vendi ..like c ondel 3 rd positionil 1 varum
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
        #python dictionary needs immutable keys.. list is mutable so we convert the count into tuple
            key = tuple(count)
        # why appending rather than =  is that ipo equal to anel last word mathrame keru like ate,nat oke ...full list kittan anu append() use cheyyune
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values() )

strs =["eat","tea","tan","ate","nat","bat"]
sol =  Solution()
print(sol.groupAnagrams(strs))

# Time : O(n * m)
# space : O(n * m)