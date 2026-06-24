class Solution:
    def climb(self, n: int, cached: List[int]) -> int:
        if n == 1 or n == 2:
            cached[n-1] = n
            return n
        prev1 = cached[n-2] if cached[n-2] > 0 else self.climb(n-1, cached)
        prev2 = cached[n-3] if cached[n-3] > 0 else self.climb(n-2, cached)
        
        cached[n-1] = prev1 + prev2
        return cached[n-1]


    def climbStairs(self, n: int) -> int:
        cached = [0] * n
        return self.climb(n, cached)