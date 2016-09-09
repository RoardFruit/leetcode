# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isM(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                return left.val==right.val and isM(left.left,right.right) and isM(left.right,right.left)
                
        if root is None:
            return True
        else:
            return isM(root.left,root.right)
            