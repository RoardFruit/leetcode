# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res=[0]
        def sumIter(tree,path):
            if tree.left is None and tree.right is None:
                res[0]=res[0]+int(path+str(tree.val))
            if tree.left is not None:
                sumIter(tree.left,path+str(tree.val))
            if tree.right is not None:
                sumIter(tree.right,path+str(tree.val))
        sumIter(root,'')
        return res[0]