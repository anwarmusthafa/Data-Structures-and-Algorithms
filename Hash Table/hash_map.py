class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for ch in key:
            h+= ord(ch)
        return h % 100
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    

    
t = HashTable()
t.add('anwar',23)
t.add('musthafa',20)
t.add('anu',10)
print(t.get('anu'))





