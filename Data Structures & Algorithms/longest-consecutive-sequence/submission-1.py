import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        heapq.heapify(nums)
        longest = 0
        last = heapq.heappop(nums)
        count = 1
        while len(nums) > 0:
            curr = heapq.heappop(nums)
            diff = curr - last
            if diff == 1:
                count+=1
            elif diff > 1:
                if count > longest: longest = count
                count = 1
            last = curr
        if count > longest: longest = count

        return longest

        
