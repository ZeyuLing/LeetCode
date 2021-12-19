# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if(head.val==val):
            head=head.next
            return head
        p=head
        while(p.next!=None):
            if(p.next.val==val):
                p.next=p.next.next
                return head
            else : p=p.next
