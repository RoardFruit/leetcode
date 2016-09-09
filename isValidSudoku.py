class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s=set()
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j]!='.':
                    if (board[i][j],i) not in s and (j,board[i][j]) not in s and (board[i][j],i/3,j/3) not in s:
                        s.add((board[i][j],i))
                        s.add((j,board[i][j]))
                        s.add((board[i][j],i/3,j/3))
                    else:
                        return False
        return True