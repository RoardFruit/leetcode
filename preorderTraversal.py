class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        res=[]
        p=root
        while stack or p:
            while p:
                stack.append(p)
                res.append(p.val)
                p=p.left
            p=stack.pop()
            p=p.right
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Iter(tree):
            if tree is None:
                return []
            else:
                return [tree.val]+Iter(tree.left)+Iter(tree.right)
        return Iter(root)