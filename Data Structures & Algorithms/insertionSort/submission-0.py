# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        process = []

        for i in range(len(pairs)):
            j = i
            while j > 0 and pairs[j].key < pairs[j-1].key:
                pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
                j-=1

            process.append(copy.deepcopy(pairs))
        
        return process
                
