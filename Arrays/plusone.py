class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1]+digits

l = Solution()
s=[9,9,6,9]
print(l.plusOne(s))





