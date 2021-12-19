# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow=head
        fast=head
        if(head==None):
            return None
        list_len=1
        while(fast.next!=None and fast.next.next!=None):
            list_len+=2
            fast=fast.next.next
        if(fast.next!=None):
            list_len+=1
        count=list_len-k
        while(count):
            slow=slow.next
            count-=1
        return slow
