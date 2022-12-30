# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    done = {}
    nums.each_with_index do |element, i|
        if done.has_key?(target-nums[i])
            return [done[target-nums[i]], i]
        end
        done[nums[i]] = i
    end
end