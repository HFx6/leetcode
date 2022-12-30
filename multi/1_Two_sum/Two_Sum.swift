class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var done = [Int: Int]()
    var sums = [Int]()
    for i in 0...nums.count-1{
        let key = target-nums[i]
        if let val = done[key] {
            sums.append(val)
            sums.append(i)
            return sums
        }
        done[nums[i]] = i
    }
    return [0]
}
}