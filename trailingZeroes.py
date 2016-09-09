class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        while n:
            n=n/5
            r=r+n
        return r