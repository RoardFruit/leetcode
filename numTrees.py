class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[1]
        for i in range(1,n+1):
            a.append(0)
            for j in range(0,i):
                a[i]+=a[j]*a[i-1-j]
        return a[n]