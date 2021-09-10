# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        currents = [root]
        
        while len(currents) > 0:
            tosend = []
            tosendvalues = []
            for i in currents:
                if i.left:
                    tosend.append(i.left)
                    tosendvalues.append(i.left.val)
                if i.right:
                    tosend.append(i.right)
                    tosendvalues.append(i.right.val)
            if len(tosendvalues) > 0:
                res.append(tosendvalues)
            currents = tosend
            
        return [[root.val]] + res