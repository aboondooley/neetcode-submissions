class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, n-1
        while l < r:
            result = numbers[l] + numbers[r]
            if result == target: return [l+1, r+1]
            if result > target: r-=1
            else: l+=1
        
        return [-1,-1]