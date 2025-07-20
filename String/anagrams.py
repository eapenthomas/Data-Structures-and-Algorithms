from collections import Counter
word1 = "silent"
word2= "listen"
word3= "listens"
counter ={}
for char in word3:
    counter[char]= counter.get(char,0)+1
print(counter)

if sorted(word1) == sorted(word2):
    print(word2 +" and "+word1+" are anagrams")
else:
    print(word2 +" and "+word1+" are not anagrams")


if Counter(word1) == Counter(word3):
    print(word3 + " and " + word1 + " are anagrams")
else:
    print(word3 + " and " + word1 + " are not anagrams")
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0]*26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all([x==0  for x in count ])


print(isAnagram(word1,word1))

