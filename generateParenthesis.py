class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def generateIter(left,right,s):
            if left==right==0:
                res.append(s)
            if left>0:
                generateIter(left-1,right,s+'(')
            if right>0 and left<right:
                generateIter(left,right-1,s+')')
        generateIter(n,n,'')
        return res