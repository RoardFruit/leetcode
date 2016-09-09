# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        l=[]
        if root is None:
            return l
        def Iter(tree,string):
            if tree.left is None and tree.right is None:
                l.append(string+str(tree.val))
            elif tree.right is None:
                Iter(tree.left,string+str(tree.val)+'->')
            elif tree.left is None:
                Iter(tree.right,string+str(tree.val)+'->')
            else:
                Iter(tree.left,string+str(tree.val)+'->')
                Iter(tree.right,string+str(tree.val)+'->')
        Iter(root,'')
        return l
        