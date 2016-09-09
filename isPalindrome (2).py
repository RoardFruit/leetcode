# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        pre=None
        while slow:
            temp=slow.next
            slow.next=pre
            pre=slow
            slow=temp
        while pre:
            if head.val!=pre.val:
                return False
            else:
                head=head.next
                pre=pre.next
        return True