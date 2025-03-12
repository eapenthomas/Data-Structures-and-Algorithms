def larg_common_prefix(strs):
    prefix = strs[0]
    for i in range(1,len(strs)):
        string = strs[i]
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


lis = ["hello","hell","hellar"]
print(larg_common_prefix(lis))