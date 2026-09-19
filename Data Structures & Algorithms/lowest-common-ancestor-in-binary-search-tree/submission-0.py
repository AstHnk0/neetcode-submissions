# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        if p.val < current.val and q.val < current.val:
            return self.lowestCommonAncestor(current.left, p, q)
        elif p.val > current.val and q.val > current.val:
            return self.lowestCommonAncestor(current.right, p, q)
        elif p.val == current.val or q.val == current.val:
            return current
        else:
            return current