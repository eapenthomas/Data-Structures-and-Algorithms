
# def inpara():
#     brackets = {')': '(', ']': '[', '{': '}'}
#     for c in s:
#         if c in brackets.values():
#             stack.append(c)
#         if stack and c in brackets:
#             if stack[-1] == brackets[c]:
#                 stack.pop()
#             else:
#                 return False
#     return not stack










stack = []
s = '([])'

def valipara():
    brackets = {')':'(','}':'{',']':'['}
    for chara in s:
        if chara in brackets.values():
            stack.append(chara)
        if chara in brackets and stack:
           if stack[-1] == brackets[chara]:
               stack.pop()
           else:
               return False
    return not stack

print(valipara())












