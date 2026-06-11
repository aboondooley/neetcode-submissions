# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(left:List[Pair], right:List[Pair]) -> List[Pair]:
            sorted = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    sorted.append(left[l])
                    l+=1
                else:
                    sorted.append(right[r])
                    r+=1
            while l < len(left):
                sorted.append(left[l])
                l+=1
            while r < len(right):
                sorted.append(right[r])
                r+=1
            return sorted
        
        def merge(pairs: List[Pair]) -> List[Pair]:
            if len(pairs) < 2:
                return pairs
            mid = len(pairs) // 2
            left= merge(pairs[:mid])
            right = merge(pairs[mid:])

            return sort(left, right)

        return merge(pairs)
