class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        num_set = set(nums)
        longest = 1
        for num in num_set:
            if num-1 not in num_set:
                length = 1
                while (num+length) in num_set:
                    length+=1
                longest = max(length, longest)
        return longest
