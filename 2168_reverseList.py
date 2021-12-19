# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        q=None
        while(p!=None):
            temp=p.next
            p.next=q
            q=p
            p=temp
        return q