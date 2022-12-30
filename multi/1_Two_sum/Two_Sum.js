/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var done = {};
    var sums = [];
    for(var i=0; i<nums.length; i++){
        if((target-nums[i]) in done){
            sums.push(done[target-nums[i]]);
            sums.push(i);
            return sums;
        }
        done[nums[i]] = i;
    };

    return sums;
};