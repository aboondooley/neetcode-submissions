class Deque:
    
    def __init__(self):
        self.size = 0
        self.values = []


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        self.values.append(value)
        self.size += 1
        

    def appendleft(self, value: int) -> None:
        self.values.insert(0, value)
        self.size += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.values.pop(self.size - 1)
        self.size -= 1
        return last
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.values.pop(0)
        self.size -= 1
        return first
        
