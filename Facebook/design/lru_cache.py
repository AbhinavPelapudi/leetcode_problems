# LRU Cache
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def assign_head(self, node):
        old_head = self.head.next
        if old_head.key == node.key:
            return
        if node.key in self.cache:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.head.next = node
        node.prev = self.head
        node.next = old_head
        old_head.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.assign_head(self.cache[key])
        return self.cache[key].value
        
    def remove_node(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cache.pop(node.key)
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.assign_head(self.cache[key])
            return
        if len(self.cache) == self.capacity:
            self.remove_node()
        new_node = Node(key, value)
        self.assign_head(new_node)
        self.cache[key] = new_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)