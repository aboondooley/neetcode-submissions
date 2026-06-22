class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                product*=nums[i]
            else:
                zero_count+=1

        products = [0 for i in range(len(nums))]
        if zero_count == 0:
            for i in range(len(nums)):
                products[i] = product//nums[i]
        elif zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    products[i] = product

        return products