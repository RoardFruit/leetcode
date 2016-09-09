class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def isVaild(x,y):
            return x>=0 and x<m and y>=0 and y<n
        for i in range(m):
            for j in range(n):
                neighLives=sum([1 for x_shift in [-1,0,1] for y_shift in [-1,0,1] if (x_shift or y_shift) and isVaild(i+x_shift,j+y_shift) and (board[i+x_shift][j+y_shift]==1 or board[i+x_shift][j+y_shift]==2)])
                if board[i][j]==1:
                    if neighLives<2 or neighLives>3:
                        board[i][j]=2
                else:
                    if neighLives==3:
                        board[i][j]=3
        for i in range(m):
            for j in range(n):
                board[i][j]=board[i][j]%2
  