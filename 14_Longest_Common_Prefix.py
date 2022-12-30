def longestCommonPrefix(strs):
    if not strs:
        return ""
    result = ""
    for characters in zip(*strs):
        if all(bin(ord(c))[2:] == bin(ord(characters[0]))[2:] for c in characters[1:]):
            result += characters[0]
        else:
            break
    return result