# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        best_level = 1
        best_sum = root.val

        while q:
            size = len(q)
            curr_sum = 0
            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curr_sum > best_sum:
                best_sum = curr_sum
                best_level = level
            level += 1

        return best_level
