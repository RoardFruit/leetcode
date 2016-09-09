class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        return reduce(lambda x,y:x*y,range(n,m+n-1))/reduce(lambda x,y:x*y,range(1,m))