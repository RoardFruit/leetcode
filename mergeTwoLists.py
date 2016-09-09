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
        l,r=l1,l2
        p=None
        while l!=None and r!=None:
            if l.val<r.val:
                if p is None:
                    head,p=l,l
                else:
                    p.next=l
                    p=p.next
                l=l.next
            else:
                if p is None:
                    head,p=r,r
                else:
                    p.next=r
                    p=p.next
                r=r.next
        if l is None:
            if p is None:
                head=r
            else:
                p.next=r
        else:
            if p is None:
                head=l
            else:
                p.next=l
        return head
#º¯ÊýÊ½µÝ¹é
def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1, l2.next)
            return l2
        