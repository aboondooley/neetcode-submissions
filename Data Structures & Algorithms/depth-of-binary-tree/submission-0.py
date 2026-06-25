# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if not root: return 0
        depth = 1
        queue.append((1, root))

        while queue:
            d, node = queue.pop()
            if d > depth: depth = d
            if node.left:
                queue.append((d+1, node.left))
            if node.right:
                queue.append((d+1, node.right))

        return depth

        