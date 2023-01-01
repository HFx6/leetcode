def letterCombinations(digits):
    t9 = {
        '2': ["a", "b", "c"],
        '3': ["d", "e", "f"],
        '4': ["g", "h", "i"],
        '5': ["j", "k", "l"],
        '6': ["m", "n", "o"],
        '7': ["p", "q", "r", "s"],
        '8': ["t", "u", "v"],
        '9': ["w", "x", "y", "z"]
    }
    combo = [''] if digits else []

    for d in digits:
        _combo = []
        for p in combo:
            for q in t9[d]:
                _combo.append(p + q)
        combo = _combo
    return combo


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
print(letterCombinations("245"))
