class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(n):
            left=0
            right=n-1
            while left<right:
                temp=matrix[i][left]
                matrix[i][left]=matrix[i][right]
                matrix[i][right]=temp
                left+=1
                right-=1
        