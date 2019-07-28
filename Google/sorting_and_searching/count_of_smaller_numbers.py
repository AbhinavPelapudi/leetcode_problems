class BNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.less_than_or_equal_count = 1


def insert(node, val):
    curr_count = 0
    while True:
        if val <= node.val:
            node.less_than_or_equal_count += 1
            if node.left:
                node = node.left
            else:
                node.left = BNode(val)
                break
        else:
            curr_count += node.less_than_or_equal_count
            if node.right:
                node = node.right
            else:
                node.right = BNode(val)
                break
    return curr_count
                
    
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        root = BNode(nums[n - 1])
        counts = [0]
        for i in range(n-2, -1,  -1):
            c = insert(root, nums[i])
            counts.append(c)
        return counts[::-1]