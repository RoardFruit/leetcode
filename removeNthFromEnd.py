# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first=head
        second=head
        i=0
        while i<n:
            first=first.next
            i=i+1
        while first:
            first=first.next
            pre=second
            second=second.next
        if second==head:
            return head.next
        else:
            pre.next=second.next
            return head
        