class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1: curr+=1
            else:
                count = max(count, curr)
                curr = 0

        return max(count, curr)