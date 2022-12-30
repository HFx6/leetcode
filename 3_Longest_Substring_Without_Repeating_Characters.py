def lengthOfLongestSubstring(s):
    cmax = 0
    for i in range(0, len(s)):
        d=''
        for m in range(i, len(s)):
            if s[m] not in d:
                d+=s[m]
            else:
                break
        cmax = max(cmax, len(d))
    return cmax