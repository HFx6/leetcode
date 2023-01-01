def isNumber(s):
    s = s.strip()
    validsymbol = ["+", "-"]
    seennonint = False
    seenint = False
    decimal = False
    large = False
    for i in range(len(s)):
        cur = s[i]
        if cur.isdigit():
            seenint = True
            continue
        elif cur in validsymbol:
            if (seennonint and not large) or \
                ((seenint or decimal) and not large) or \
                    (large and seenint) or \
                    i==len(s)-1:
                return False
            seennonint = True
        elif cur == "." and not large and not decimal:
            decimal = True
        elif cur in ["e", "E"] and seenint and not large:
            large = True
            seenint = False
        else:
            return False
    return seenint