class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map and map[diff] is not i:
                return [i,map[diff]]
        return [-1,-1]