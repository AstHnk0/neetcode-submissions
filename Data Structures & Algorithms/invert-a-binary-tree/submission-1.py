# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()

                tmp = curr.left
                curr.left = curr.right
                if curr.left:
                    queue.append(curr.left)

                curr.right = tmp
                if curr.right:
                    queue.append(curr.right)
        return root

        