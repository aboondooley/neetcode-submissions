class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        second = [0] * (2*n)
        for i,num in enumerate(nums):
            second[i] = second[i+n] = num

        return second