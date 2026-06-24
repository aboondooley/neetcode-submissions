class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1: return nums[0]
        
        rob1, rob2 = 0,0

        for num in nums:
            curr = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = curr
        return rob2