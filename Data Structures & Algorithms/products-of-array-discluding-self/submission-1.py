class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                product*=nums[i]
            else:
                zero_count+=1

        products = [0] * n
        if zero_count == 0:
            for i in range(n):
                products[i] = product//nums[i]
        elif zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    products[i] = product

        return products