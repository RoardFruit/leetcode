class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(a,b,t):
            if t==n:
                return b
            else:
                return climb(b,a+b,t+1)
        return climb(1,1,1)