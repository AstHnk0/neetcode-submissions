#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        arr = []
        if root:
            queue.append(root)
        else:
            return arr
        curr = root
        arr.append(curr.val)
        while queue:
            for k in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if queue:
                right = queue[-1]
                arr.append(right.val)
        return arr