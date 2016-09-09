# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSame(p,q):
            if p is None and q is None:
                return True
            elif p is None and not q is None:
                return False
            elif q is None and not p is None:
                return False
            else:
                return isSame(p.left, q.left) and p.val==q.val and isSame(p.right, q.right)
        return isSame(p,q)