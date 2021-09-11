# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        hold = head
        
        while head.next:
            head = head.next
            length += 1
        head.next = hold
        
        for i in range((length - k) % length):
            hold = hold.next
        head = hold
        
        for i in range(length - 1):
            head = head.next
        head.next = None
        
        return hold
        
            