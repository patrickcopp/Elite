# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number_one=[]
        current=l1
        while current!=None:
            number_one.insert(0,str(current.val))
            current=current.next
        number_one=int(''.join(number_one))
        
        number_two=[]
        current=l2
        while current!=None:
            number_two.insert(0,str(current.val))
            current=current.next
        number_two=int(''.join(number_two))
        
        total=list(str(number_one+number_two))
        
        header=None
        prev_node=None
        
        for each in total:
            header=ListNode(each)
            header.next=prev_node
            prev_node=header
        
        return header