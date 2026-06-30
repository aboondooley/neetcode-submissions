class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        min_h = [0] * n
        total_water = 0

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        for i in range(n):
            min_h[i] = min(max_left[i], max_right[i])
        for i in range(n):
            total_water+=max(0, min_h[i]-height[i])

        return total_water
