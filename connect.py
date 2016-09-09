
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return 
        p=root
        while p.left:
            q=p
            while q:
                q.left.next=q.right
                if q.next:
                    q.right.next=q.next.left
                q=q.next
            p=p.left

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def Iter(left,right):
            if left and right:
                left.next=right
                Iter(left.left,left.right)
                Iter(left.right,right.left)
                Iter(right.left,right.right)
        if root:
            Iter(root.left,root.right)
