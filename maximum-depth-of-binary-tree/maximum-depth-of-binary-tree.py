# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node):
        if not node:
            return 0
        return 1 + max(self.recurse(node.left), self.recurse(node.right))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.recurse(root.left), self.recurse(root.right))
    
    
            
        
        
    
            