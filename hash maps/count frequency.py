from collections import Counter
text = "helloworld"
char_counter = Counter(text)
s = sorted(char_counter.values())
print(s)
print(char_counter.values())
s = max(char_counter.values())
print(s)
# text =set(text)
# for i in text:
#     print(i + " count = ",char_counter[i])