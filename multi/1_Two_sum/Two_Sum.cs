public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] sums = new int[2];
        IDictionary<int, int> done = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++){
            if(done.ContainsKey(target-nums[i])){
                sums[0]=done[target-nums[i]];
                sums[1]=i;
                return sums;
            }
            done[nums[i]] = i;
        }
        return sums;
    }
}