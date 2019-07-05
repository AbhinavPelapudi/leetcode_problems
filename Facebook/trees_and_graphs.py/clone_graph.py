# Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
1 -- 2
|    |
4 -- 3
seen = {1, 2, 4}
q = [3]
Node(1).neighbors = [2, 4]
Node(2).neighbors = [1, 3]
Node(4).neighbors = [1, 3]
Node(3).neighbors = [2, 4]
copy_nodes = {1: Node(1), 2: Node(2), 4: Node(4), 3: Node(3)}

"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = deque()
        q.append(node)
        copy_nodes = {}
        root = Node(node.val, [])
        copy_nodes[node.val] = root
        seen = set([node])
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in copy_nodes:
                    copy_nodes[neighbor.val] = Node(neighbor.val, [])
                copy_nodes[node.val].neighbors.append(copy_nodes[neighbor.val])
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
        return root