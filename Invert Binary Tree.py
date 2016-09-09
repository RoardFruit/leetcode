# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(tree):
            if tree is None:
                pass
            else:
                temp=tree.left
                tree.left=tree.right
                tree.right=temp
                invert(tree.left)
                invert(tree.right)
        invert(root)
        return root

º¯ÊýÊ½µÝ¹é
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(tree):
            if tree is None:
                return tree
            else:
                left=invert(tree.left)
                right=invert(tree.right)
                tree.left=right
                tree.right=left
                return tree
        return invert(root)