class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        print("Key not found")

hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 15)

print("Search apple:", hash_table.search("apple"))
print("Search banana:", hash_table.search("banana")) 
print("Search orange:", hash_table.search("orange"))  

hash_table.delete("banana")
print("Search banana after deletion:", hash_table.search("banana")) 
