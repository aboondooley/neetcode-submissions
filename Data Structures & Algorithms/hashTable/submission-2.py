class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [[] for _ in range(capacity)]
        self.size = 0
        self.capacity = capacity


    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        row = self.table[hash_key]
        for i in range(len(row)):
            if row[i].key == key:
                row[i].value = value
                return
        row.append(Pair(key, value))
        self.size+=1
        if self.size * 2 >= self.capacity:
            self.resize()


    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        for r in self.table[hash_key]:
            if r.key == key:
                return r.value
        return -1

    def remove(self, key: int) -> bool:
        hash_key = self.hash(key)
        row = self.table[hash_key]
        new_row = []
        found = False
        for pair in row:
            if pair.key != key:
                new_row.append(pair)
            else:
                found = True
                self.size-=1
        self.table[hash_key] = new_row
        return found


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity*=2
        new_table = [[] for _ in range(self.capacity)]
        for row in self.table:
            for r in row:
                new_hash = self.hash(r.key)
                new_table[new_hash].append(Pair(r.key, r.value))
        self.table = new_table

    def hash(self, key) -> int:
        return key % self.capacity

