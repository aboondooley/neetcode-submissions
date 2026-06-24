class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return min(cost)

        for i in range(2, n):
            one, two = cost[i-1], cost[i-2]
            curr = cost[i]
            cost[i] = cost[i]
            cost[i] = min(curr+one, curr+two)

        return min(cost[-1], cost[-2])
