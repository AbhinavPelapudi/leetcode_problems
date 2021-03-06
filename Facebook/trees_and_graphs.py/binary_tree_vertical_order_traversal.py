# Binary Tree Vertical Order Traversal
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
distances = {0: [3, 0, 1], -1: [9, 5], 1: [8, 2], -2: [4], 2: [7]}
node_pose = {3: 0, 9: -1, 8: 1, 4: -2, 0: 0, 7: 2, 1: 0}
result = []
q = []
point = 0 
min_d = -2
max_d = 2

[4]
[9, 5]
[3, 0, 1]
[8, 2]
[7]

"""
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        distances = defaultdict(list)
        node_pos = defaultdict()
        distances[0].append(root.val)
        result = []
        q = deque()
        point = 0 
        min_d, max_d = 0, 0
        node_pos[root] = point
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                distances[node_pos[node] - 1].append(node.left.val)
                q.append(node.left)
                node_pos[node.left] = node_pos[node] - 1
                if node_pos[node.left] < min_d:
                    min_d = node_pos[node.left]
            if node.right:
                distances[node_pos[node] + 1].append(node.right.val)
                q.append(node.right)
                node_pos[node.right] = node_pos[node] + 1
                if node_pos[node.right] > max_d:
                    max_d = node_pos[node.right]
        for i in range(min_d, max_d + 1):
            result.append(distances[i])
        return result