class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        nums.sort()

        for i in range(n):
            a = nums[i]
            if a > 0: break
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0: l+=1
                elif s > 0: r-=1
                else:
                    results.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1
                    while l < r and nums[r] == nums[r+1]: r-=1

        return results