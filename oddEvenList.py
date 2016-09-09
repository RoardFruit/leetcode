# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        pre=head
        prenode=head.next
        node=prenode.next
        while node:
            prenode.next=node.next
            node.next=pre.next
            pre.next=node
            pre=node
            prenode=prenode.next
            if prenode is None:
                node=None
            else:
                node=prenode.next
        return head