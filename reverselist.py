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
        if head:
            pre=head
            next=head.next
            head.next=None
            while next:
                temp=next.next
                next.next=pre
                pre=next
                next=temp
            return pre
        else:
            return head
                
                
            