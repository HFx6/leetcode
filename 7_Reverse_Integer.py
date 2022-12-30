def reverse(x):
    s = str(abs(x))
    s = s[::-1]
    if x<0 and -0x80000000&-abs(int(s))==-0x80000000:
        return -abs(int(s))
    if int(s)&0x7fffffff==int(s):
        return int(s)
    return 0