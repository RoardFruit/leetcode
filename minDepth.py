# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minDepthIter(tree):
            if tree is None:
                return 0
            if tree.left is None and tree.right is None:
                return 1
            elif tree.left is None:
                return minDepthIter(tree.right)+1
            elif tree.right is None:
                return minDepthIter(tree.left)+1
            else:
                return min(minDepthIter(tree.left),minDepthIter(tree.right))+1
        return minDepthIter(root)
        