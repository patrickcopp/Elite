class Node:
    prev = None
    next = None
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __repr__(self):
        return str(self.key)+" "+ str(self.val)

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.mapper = {}
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.mapper:
            node = self.mapper[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            node = self.mapper[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            self.size += 1
            if self.size > self.capacity:
                del self.mapper[self.tail.prev.key]
                self.remove(self.tail.prev)
                self.size -= 1
            node = Node(key,value)
            self.add(node)
            self.mapper[key] = node
            
            
    def add(self, node):
        head_next = self.head.next
        node.next = head_next
        head_next.prev = node
        
        self.head.next = node
        node.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        next.prev = prev
        prev.next = next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)