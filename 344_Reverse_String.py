def reverseString(s):
    l = len(s)
    for i in range(l//2):
        s[i], s[l-1-i] = s[l-1-i], s[i]
