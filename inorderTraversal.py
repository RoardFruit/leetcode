# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def Iter(tree):
            if tree is None:
                pass
            else:
                Iter(tree.left)
                res.append(tree.val)
                Iter(tree.right)
        Iter(root)
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Iter(tree):
            if tree is None:
                return []
            else:
                return Iter(tree.left)+[tree.val]+Iter(tree.right)
        return Iter(root)