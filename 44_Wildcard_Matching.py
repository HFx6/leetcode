def isMatch(s, p):
    m = [[False for l in range(len(p)+1)] for i in range(len(s)+1)]
    m[0][0] = True
    for i in range(1, len(p)+1):
        if p[i-1] != '*':
            break
        m[0][i] = True
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] in [s[i-1], '?']:
                m[i][j] = m[i-1][j-1]
            elif p[j-1] == '*':
                m[i][j] = m[i-1][j] or m[i][j-1]
    return m[-1][-1]