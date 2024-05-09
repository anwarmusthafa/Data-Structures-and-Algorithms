class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        raise KeyError(key)

    def delete(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                return
        raise KeyError(key)

    def display_items(self):
        print("Key-Value pairs in the hash table:")
        for item in self.arr:
            if item:
                for k, v in item:
                    print(f"Key: {k}, Value: {v}")


# Testing the hash table
t = HashTable()
t.add('anwar', 23)
t.add('musthafa', 20)
t.add('anu', 10)
t.add('name','anwar')
t.add('mane','musthafa')
t.add('name',"new")
t.display_items()
print(t.arr)
