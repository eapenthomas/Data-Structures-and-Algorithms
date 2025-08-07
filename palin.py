class Solution:
    def palin(self,num):
        r = 0
        n = num
        while num>0:
            b = num%10
            r = r*10+b
            num = num//10
        return r==n
sol =Solution()
print(sol.palin(545))

