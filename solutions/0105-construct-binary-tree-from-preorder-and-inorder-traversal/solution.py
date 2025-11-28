# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {v:i for i,v in enumerate(inorder)}
        self.pre_i = 0
        def helper(l, r):
            if l > r:
                return None
            root_val = preorder[self.pre_i]
            self.pre_i += 1
            root = TreeNode(root_val)
            mid = idx_map[root_val]
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        return helper(0, len(inorder) - 1)

