def romanToInt(s):
    rti = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000}
    v = 0
    for i in range(0, len(s) - 1):
        cur = s[i]
        next = s[i + 1]
        if rti[next] > rti[cur]:
            v -= rti[cur]
        else:
            v += rti[cur]
    v += rti[s[-1]]
    return v
