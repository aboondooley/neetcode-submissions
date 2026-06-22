from _heapq import heapify
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            if n not in freq_map:
                freq_map[n] = 0
            freq_map[n]+=1

        items_list = [(-freq, value) for value,freq in freq_map.items()]
        heapify(items_list)
        
        top_k = []
        for i in range(k):
            freq, value = heappop(items_list)
            top_k.append(value)

        return top_k

        
