# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        follower = head
        while l1 and l2:
            if l1.val < l2.val:
                follower.next = l1
                l1 = l1.next
            else:
                follower.next = l2
                l2 = l2.next
            follower = follower.next
                
        if l1:
            follower.next = l1
        elif l2:
            follower.next = l2
        
        return head.next