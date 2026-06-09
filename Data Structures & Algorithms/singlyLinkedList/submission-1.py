class Node:
    def __init__(self, value, node):
        self.value = value
        self.next = node


class LinkedList:
    
    def __init__(self):
        self.head = Node(0, None)
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        here = self.head.next
        for i in range(index):
            here = here.next
        return here.value

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head.next)
        self.head.next = newNode
        self.size += 1
        
    def insertTail(self, val: int) -> None:
        here = self.head
        while here.next:
            here = here.next
        here.next = Node(val, None)
        self.size += 1
        
    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        here = self.head
        for i in range(index):
            here = here.next
        nextNode = here.next.next
        here.next = nextNode
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        here = self.head.next
        while here:
            values.append(here.value)
            here = here.next
        return values
