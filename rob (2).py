# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m={}
        def maxProfit(tree):
            if tree is None:
                return 0
            val=m.get(tree,0)
            if val:
                return val
            sum=0
            if tree.left:
                sum+=maxProfit(tree.left.left)+maxProfit(tree.left.right)
            if tree.right:
                sum+=maxProfit(tree.right.left)+maxProfit(tree.right.right)
            val=max(sum+tree.val,maxProfit(tree.left)+maxProfit(tree.right))
            m[tree]=val
            return val
        return maxProfit(root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxProfit(tree):
            val=[0,0]
            if tree is None:
                return val
            left=maxProfit(tree.left)
            right=maxProfit(tree.right)
            val[0]=max(left)+max(right)
            val[1]=tree.val+left[0]+right[0]
            return val
        return max(maxProfit(root))