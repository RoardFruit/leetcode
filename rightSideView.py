# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Iter(tree):
            if tree is None:
                return []
            left=Iter(tree.left)
            right=Iter(tree.right)
            ln=len(left)
            rn=len(right)
            if ln<=rn:
                return [tree.val]+right
            else:
                return [tree.val]+right+left[rn:]
        return Iter(root)
                