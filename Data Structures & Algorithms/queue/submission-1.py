# Linked List solution
from typing import Self

class Node:
    def __init__(self, val: int, prev: Optional[Self|None], next: Optional[Self|None]):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.size = 0
        self.tail = Node(-1, None, None)
        self.head = Node(-1, None, self.tail)
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        node = Node(value, self.tail.prev, self.tail)
        self.tail.prev = node
        node.prev.next = node
        self.size += 1
        
        

    def appendleft(self, value: int) -> None:
        node = Node(value, self.head, self.head.next)
        self.head.next = node
        node.next.prev = node
        self.size += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return value
        

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        value = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return value

        
