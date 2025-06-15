class lenstring:
    def countlastword(self,s):
        count = 0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                break
            count = count + 1
        return count
l = lenstring()
print(l.countlastword("helo wor  "))