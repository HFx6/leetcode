def twoSum(nums, target):
    done = {}
    for i in range(len(nums)):
        if(done.get(target-nums[i])!=None):
            return [done[target-nums[i]], i]
        done[nums[i]] = i