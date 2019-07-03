# time: O(1)
# space: O(n)
# LRU Cache

"""
self.capacity = 3
start: Node(start) -> Node(end)
                   <-

add(1:1)
cache = {1: Node(1)}
Node(start) -> Node(1) -> Node(end)
            <-        <-

add(2:2)
cache = {1: Node(1), 2: Node(2)}
Node(start) -> Node(2) -> Node(1) -> Node(end)
            <-        <-          <-   

add(3:2)
cache = {1: Node(1), 2: Node(2), 3, Node(3)}

Node(start) -> Node(3)-> Node(2) -> Node(1) -> Node(end)
            <-        <-        <-          <-   

add(4:4)
Node(start) -> Node(4) -> Node(3)-> Node(2) -> Node(end)
            <-        <-        <-          <-

get(3, 2)
Node(start) -> Node(3)-> Node(4) ->  Node(2) -> Node(end)
            <-        <-        <-          <-

"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity #assign capacity
        self.cache = {} #set cache
        self.head = Node(None, None) #assign head
        self.tail = Node(None, None) #assign tail
        self.head.next = self.tail #create relationship between head and tail
        self.tail.prev = self.head

    def assign_head(self, node):
        old_head = self.head.next
        if old_head.key == node.key:
            return
        if node.key in self.cache: #remove from its original position
            node.prev.next = node.next
            node.next.prev = node.prev
        self.head.next = node # reassign and shift down
        node.prev = self.head
        node.next = old_head
        old_head.prev = node
    
    def get(self, key: int) -> int: #shifts up when retrieved 
        if key not in self.cache:
            return -1
        self.assign_head(self.cache[key])
        return self.cache[key].value
        
    def remove_node(self): #using the tail, remove node
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cache.pop(node.key)
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache: #reassigns value if it exists
            self.cache[key].value = value
            self.assign_head(self.cache[key])
            return
        if len(self.cache) == self.capacity: #if at capacity, remove last node
            self.remove_node()
        new_node = Node(key, value) #create new node
        self.assign_head(new_node) #assign head
        self.cache[key] = new_node #cache the node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)