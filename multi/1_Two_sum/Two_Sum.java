import java.util.HashMap; 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sums = new int[]{0,1};
        Map<Integer, Integer> done = new HashMap<Integer, Integer>(); 
        int ex;

        for (int i = 0; i < nums.length; i++) {
            if(done.containsKey(target-nums[i])){
                sums = new int[]{done.get(target-nums[i]), i};
                break;
            }
            done.put(nums[i], i);
        }
        return sums;
    }
}