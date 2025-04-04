# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l=[]
        a=list1
        while a is not None:
            l.append(a.val)
            a=a.next
        b=list2
        while b is not None:
            l.append(b.val)
            b=b.next
        l.sort()
        dummy = ListNode(0)
        current = dummy
        for val in l:
            current.next = ListNode(val)
            current = current.next

        return dummy.next