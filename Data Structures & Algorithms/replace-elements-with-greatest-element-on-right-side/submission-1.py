class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def find_max(nums):
            max_val = -1
            index = -1
            for i,num in enumerate(nums):
                if num > max_val:
                    max_val = num
                    index = i
            return (index, max_val)

        new_arr = [0] * len(arr)
        index, max_val = find_max(arr)
        for i,n in enumerate(arr):
            if i == len(arr)-1: continue
            if i >= index:
                index, max_val = find_max(arr[i+1:])

            new_arr[i] = max_val

        new_arr[-1] = -1
        return new_arr
            


