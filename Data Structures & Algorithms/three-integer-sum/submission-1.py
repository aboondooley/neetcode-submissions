class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # saving triplets that add to zero
        triplet = set()
        values = defaultdict(int)

        nums.sort()

        for n in nums:
            values[n]+=1

        for i in range(len(nums)):
            if nums[i] in values and values[nums[i]] > 0:
                values[nums[i]]-=1
                for j in range(i+1, len(nums)):
                    if nums[j] in values and values[nums[j]] > 0:
                        values[nums[j]]-=1
                        curr_sum = nums[i] + nums[j]
                        diff = 0 - curr_sum
                        if diff in values and values[diff] > 0:
                            triplet.add((nums[i],nums[j],diff))
                        
                for j in range(i+1, len(nums)):
                    values[nums[j]]+=1

        return list(triplet)
        











        return list(triplet)