class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value


class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [[] for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0


    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        is_new = True
        for pair in self.table[hash_key]:
            if pair.key == key:
                pair.value = value
                is_new = False
                break
        if is_new:
            pair = Pair(key, value)
            self.table[hash_key].append(pair)
            self.size+=1
            if self.size / self.capacity >= 0.5:
                self.resize()


    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        values = self.table[hash_key]
        for val in values:
            if val.key == key:
                return val.value
        return -1


    def remove(self, key: int) -> bool:
        hash_key = self.hash(key)
        contains = False
        new_row = []
        for pair in self.table[hash_key]:
            if pair.key != key:
                new_row.append(pair)
            else:
                contains = True
                self.size-=1
        self.table[hash_key] = new_row
        return contains


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_table = self.table
        self.capacity*=2
        new_table = [[] for _ in range(self.capacity)]
        for row in old_table:
            for pair in row:
                new_hash = self.hash(pair.key)
                new_table[new_hash].append(pair)
        self.table = new_table


    def hash(self, val: int) -> int:
        return val % self.capacity
