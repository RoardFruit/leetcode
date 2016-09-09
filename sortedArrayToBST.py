# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def Iter(start,to):
            if start>to:
                return None
            elif start==to:
                return TreeNode(nums[start])
            mid=(start+to)/2
            node=TreeNode(nums[mid])
            node.left=Iter(start,mid-1)
            node.right=Iter(mid+1,to)
            return node
        return Iter(0,len(nums)-1)