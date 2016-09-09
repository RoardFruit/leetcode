# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        if p is None or p.next is None:
            return head
        q=p.next
        p.next=q.next
        q.next=p
        head=q
        while not p.next is None and not p.next.next is None:
            pre=p
            q=p.next.next
            p=p.next
            pre.next=q
            p.next=q.next
            q.next=p
        return head