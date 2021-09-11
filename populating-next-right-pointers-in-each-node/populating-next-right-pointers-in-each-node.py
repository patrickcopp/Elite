"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':        
        if not root:
            return root
        return self.dfs(root)
        
    def dfs(self, root:'Node') -> 'Node':
        if not root.left:
            return root        
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
            
        self.connect(root.right)
        self.connect(root.left)
            
        return root