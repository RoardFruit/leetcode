# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#当左右深度超过1，可以报异常来跳出递归
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Iter(tree):
            if tree is None:
                return 0
            else:
                l=Iter(tree.left)
                r=Iter(tree.right)
                if l==-1 or r==-1 or abs(l-r)>1:
                    return -1
                else:
                    return max(l,r)+1
        if Iter(root)==-1:
            return False
        else:
            return True
            
            