# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(inorder[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        dfs(root)
        return build(0, len(inorder) - 1)
