def longestSubstring(str):
    if not str:
        return 0
    curLength = 0
    maxLength = 0
    curresult = []
    maxresult = []

    position = [-1 for i in range(26)]

    for i in range(len(str)):
        preIndex = position[ord(str[i])-ord('a')]
        if preIndex < 0 or i - preIndex > curLength:
            curLength += 1
            curresult += str[i]
        else:
            if maxLength < curLength:
                maxLength = curLength
                maxresult = curresult
            curLength = i - preIndex
            curresult = str[preIndex+1:i+1]
        position[ord(str[i])-ord('a')] = i
    if curLength > maxLength:
        maxLength = curLength
        maxresult = curresult
    return maxLength,maxresult
def Test():
    str1 = 'arabcacfr'
    str2 = 'a'
    str3 = 'aaaaa'
    str4 = 'abcde'
    str5 = None
    print(longestSubstring(str1))
    print(longestSubstring(str2))
    print(longestSubstring(str3))
    print(longestSubstring(str4))
    print(longestSubstring(str5))

Test()