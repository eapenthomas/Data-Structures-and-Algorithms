def longestCommonPrefix (strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1,len(strs)):
        strings = strs[i]
        while not strings.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix








print(longestCommonPrefix(["flower", "flow", "fpoght"]))