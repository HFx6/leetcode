def myAtoi(s):
    MIN, MAX = -2 ** 31, 2 ** 31 - 1
    bef = s.strip()
    r = ""
    signs = ["+", "-"]
    if len(bef)==0 or not bef[0].isdigit() and bef[0] not in signs:
        return 0
    for i in range(len(bef)):
        try:
            if bef[i] in signs and bef[i+1].isdigit() and len(r)==0:
                r+=bef[i]
            elif bef[i].isdigit():
                r+=bef[i]
            else:
                break 
        except IndexError:
            break
    return max(MIN, min(int(r or 0), MAX))