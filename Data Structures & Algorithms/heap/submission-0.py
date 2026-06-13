class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val: int) -> None:
        self.heap.append(val)
        index = self.size
        self.size += 1
        parent = get_parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = get_parent(index)

    def pop(self) -> int:
        if self.size == 0: return -1
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.sift_down(0)
        return root

    def top(self) -> int:
        if self.size == 0: return -1
        return self.heap[0]
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums[:]
        self.size = len(nums)
        for i in range(get_parent(self.size - 1), -1, -1):
            self.sift_down(i)

    def sift_down(self, index) -> int:
        while get_left_child(index) < self.size:
            left, right = get_left_child(index), get_right_child(index)
            smallest = left
            if right < self.size and self.heap[right] < self.heap[left]:
                smallest = right
            
            if self.heap[index] > self.heap[smallest]:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
        return index
        
def get_parent(index: int) -> int:
    return (index - 1) // 2

def get_left_child(index: int) -> int:
    return index * 2 + 1

def get_right_child(index: int) -> int:
    return index * 2 + 2