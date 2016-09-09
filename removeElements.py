# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node=head
        pre=None
        while node:
            if node.val==val:
                if pre is None:
                    head=head.next
                    node=head
                else:
                    pre.next=node.next
                    node=pre.next
            else:
                pre=node
                node=node.next
        return head