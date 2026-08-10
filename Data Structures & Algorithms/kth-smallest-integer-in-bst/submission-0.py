# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None
        def dfs(root, k) -> int:
            nonlocal count, answer
            if not root or answer is not None:
                return
            left = dfs(root.left, k)
            count += 1
            if count == k:
                answer = root.val
                return
            right = dfs(root.right, k)
        dfs(root, k)
        return answer