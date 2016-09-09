class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        i=1
        while i<=numRows:
            j=1
            while j<=i:
                if j==1:
                    l.append([1])
                elif j==i:
                    l[i-1].append(1)
                else:
                    l[i-1].append(l[i-2][j-2]+l[i-2][j-1])
                j=j+1
            i=i+1
        return l
            