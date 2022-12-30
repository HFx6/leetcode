#include <algorithm>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sums;
        unordered_map<int, int> done;
        for (int i=0;i<nums.size();i++){
            if(done.find(target - nums[i])!=done.end()){
                sums = {done[target - nums[i]], i};
                break;
            }
            done[nums[i]] = i;
        }
        return sums;
    }
};