# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        l=[]
        if root is None:
            return False
        def Iter(tree,count):
            if tree.left is None and tree.right is None:
                l.append(count+tree.val)
            else:
                if not tree.left is None:
                    Iter(tree.left,count+tree.val)
                if not tree.right is None:
                    Iter(tree.right,count+tree.val)
        Iter(root,0)
        return sum in l
                