# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=l1
        q=l2
        r=0
        result=None
        while(p!=None or q!=None):
            if(p==None):a=0
            else: a=p.val
            if(q==None):b=0
            else: b=q.val
            t = ListNode(val=(a + b + r) % 10)
            if(result!=None):
                result.next=t
            else:
                head=t
            result=t
            r=(a+b+r)/10
            if(p!=None):p=p.next
            if(q!=None):q=q.next
        if r!=0:
            t=ListNode(val=r)
            result.next=t
            result=result.next
        return head