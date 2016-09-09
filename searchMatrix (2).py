class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        col=[row[0] for row in matrix]
        def binarySearch(num,target):
            n=len(num)
            low,high=0,n-1
            while low<=high:
                mid=(low+high)/2
                if num[mid]==target:
                    return mid
                elif num[mid]<target:
                    low=mid+1
                else:
                    high=high-1
            return high
        x=binarySearch(col,target)
        print x
        if col[x]==target:
            return True
        else:
            y=binarySearch(matrix[x],target)
            print y
            if matrix[x][y]==target:
                return True
            else:
                return False