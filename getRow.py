class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a=[1]*(rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i):
                if j==0 or j==i:
                    a[j]=1
                else:
                    a[i-j]=a[i-j]+a[i-j-1]
        return a