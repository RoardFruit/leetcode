class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2 or n==3:
            return n-1
        res=1
        while n>4:
            res*=3
            n-=3
        res*=n
        return res