def permute(nums):
    permus = []
    for i in range(len(nums)):
        for p in permute(nums[:i] + nums[i+1:]):
            permus.append([nums[i]] + p)
    return permus if permus else [[]]


print(permute([1,2,3]))
print(permute([0, 1]))
print(permute([1]))