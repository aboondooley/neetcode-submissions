class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(street):
            if not street: return 0
            n = len(street)
            if n == 0: return 0
            if n == 1: return street[0]
            if n == 2: return max(street[0], street[1])

            # calculate first house
            rob1, rob2 = 0, 0

            for house in street:
                curr = max(rob1+house, rob2)
                rob1 = rob2
                rob2 = curr

            # calculate last house
            return rob2

        return max(nums[0], rob_linear(nums[1:]), rob_linear(nums[:-1]))
        

