# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        while head:
            if head.val == "cycle":
                return True
            head.val = "cycle"
            head = head.next
        return False