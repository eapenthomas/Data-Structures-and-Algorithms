s="pqrs"
t="apsdqcvfr"
i, j = 0, 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
print( i == len(s))
