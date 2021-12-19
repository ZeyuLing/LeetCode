# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=l1
        q=l2
        head=ListNode(-1)
        r=head
        while(p!=None and q!=None):
            if(p.val<q.val):
                r.next=p
                p=p.next
            else :
                r.next=q
                q=q.next
            r=r.next
        if(p!=None):
            r.next=p
        if(q!=None):
            r.next=q
        return head.next

