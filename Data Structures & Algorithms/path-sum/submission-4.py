# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = []
        answer = False
        def backtrack(root,targetSum):
            nonlocal arr, answer
            if not root:
                return False
            arr.append(root.val)
            if not root.left and not root.right and sum(arr) == targetSum:
                answer = True
                return True
            if backtrack(root.left, targetSum):
                return True
            if backtrack(root.right, targetSum):
                return True
            arr.pop()
            return False
        backtrack(root, targetSum)
        return answer