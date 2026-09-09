
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)

            oldToNew[node] = copy

            for neighbor in node.neighbors:
                neighborCopy = dfs(neighbor)
                copy.neighbors.append(neighborCopy)
            return copy
        return dfs(node)
        


