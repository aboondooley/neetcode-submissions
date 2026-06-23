class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            diff = target - numbers[i]

            # binary search
            l, r = i+1, n-1
            while i < l <= r < n:
                mid = (r+l)//2
                if diff == numbers[mid]: return [i+1,mid+1]
                elif diff > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return [-1,-1]
