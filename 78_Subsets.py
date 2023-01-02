def subsets(nums):
    subs = [[]]
    for num in nums:
        subs += [sub + [num] for sub in subs]
    return subs