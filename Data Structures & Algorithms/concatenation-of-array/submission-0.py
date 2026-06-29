class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        second = []
        for num in nums:
            second.append(num)

        return nums + second