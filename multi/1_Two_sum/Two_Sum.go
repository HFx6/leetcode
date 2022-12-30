func twoSum(nums []int, target int) []int {
    var sums []int
    done := make(map[int]int)
    
    for i, _ := range nums {
        _, ok := done[target-nums[i]]
        if ok {
            sums = append(sums, done[target-nums[i]])
            sums = append(sums, i)
            return sums
        }
	    done[nums[i]] = i
    }
    return sums
}