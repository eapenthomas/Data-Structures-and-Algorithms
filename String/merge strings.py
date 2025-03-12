class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str = ""
        m = len(word1)
        n = len(word2)
        k = max(m, n)
        for i in range(k):
            if i < m:
                merged_str += word1[i]
            if i < n:
                merged_str += word2[i]
        return merged_str

sol =Solution()
print(sol.mergeAlternately("abc","pqsr"))