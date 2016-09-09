# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        class findException(Exception):
            pass
        res=[None]
        k=[k]
        def Iter(tree):
            if tree is None:
                pass
            else:
                Iter(tree.left)
                k[0]=k[0]-1
                if k[0]==0:
                    res[0]=tree.val
                    raise findException()
                Iter(tree.right)
        try:
            Iter(root)
        except:
            return res[0]