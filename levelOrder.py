# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l=[]
        def insert(node,n):
            if node is None:
                pass
            else:
                try:
                    l[n].append(node.val)
                except:
                    l.append([node.val])
                insert(node.left,n+1)
                insert(node.right,n+1)
        insert(root,0)
        return l