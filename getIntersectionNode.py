# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA=headA
        pB=headB
        if pA is None or pB is None:
            pass
        else:
            while pA or pB:
                if not pA:
                    pA=headB
                if not pB:
                    pB=headA
                if pA==pB:
                    return pA
                pA=pA.next
                pB=pB.next