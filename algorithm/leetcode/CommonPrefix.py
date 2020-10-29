
def longestCommonPrefix(strs):

    """长度最小的字符串"""
    prefix = strs[0]

    for s in strs:
        if len(s) <= len(prefix):
            prefix = s

    if len(prefix) == 0:
        return ""

    while 1:
        flag = 1
        for s in strs:
            if s.startswith(prefix):
                continue
            else:
                flag = 0
                prefix = prefix[0:len(prefix)-1]
                break
        if flag == 1:
            break

    return prefix


if __name__ == '__main__':
    list = ["flower","flow","flight"]
    result = longestCommonPrefix(list)
    print(result)

