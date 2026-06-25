class Node:
    def __init__(self, key: int, value: int, prev: Optional["Node"] = None, nxt: Optional["Node"] = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def insert(self, node):
        node.prev = self.tail.prev
        node.nxt = self.tail
        node.prev.nxt = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.nxt
            self.remove(lru)
            self.cache.pop(lru.key)


