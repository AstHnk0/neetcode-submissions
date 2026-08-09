class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right:
            return False

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return True



        