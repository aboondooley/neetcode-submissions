class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def find_largest(nums):
            largest = -1
            for i in range(len(nums)):
                if nums[i] > largest:
                    largest = nums[i]
            return largest
        

        for i in range(len(arr)):
            arr[i] = find_largest(arr[i+1:])

        return arr