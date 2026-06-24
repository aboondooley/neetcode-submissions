import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = []
    for a in arr:
        heapq.heappush(heap, -a)

    while len(heap) > 1:
        heapq.heappop(heap)
    return -heapq.heappop(heap)



def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    elements = []
    heapq.heapify(arr)
    for i in range(4):
        elements.append(heapq.heappop(arr))
    return elements


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    elements = []
    heapq.heapify(arr)
    for i in range(2):
        elements.insert(0,(heapq.heappop(arr)))
    return elements


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

