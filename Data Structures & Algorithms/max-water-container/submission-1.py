class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = -1

        for i in range(len(heights)-1):
            r = len(heights)-1
            while i < r:
                curr_water = abs(i-r) * min(heights[i], heights[r])
                max_water = max(max_water, curr_water)
                r-=1
            
        return max_water