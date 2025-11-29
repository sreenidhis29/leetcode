# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}
        self.post_i = len(postorder) - 1
        def helper(l, r):
            if l > r:
                return None
            root_val = postorder[self.post_i]
            self.post_i -= 1
            root = TreeNode(root_val)
            m = idx[root_val]
            root.right = helper(m + 1, r)
            root.left = helper(l, m - 1)
            return root
        return helper(0, len(inorder) - 1)
