class Solution:
    def solveNQueens(self, n):
        board = [ ['.'] * n  for _ in range(n)]
        result = []
        emptyCol = [ True ] * n
        empty45 = [ True ] * (2*n-1)
        empty135 = [ True ] * (2*n-1)

        def backTracking(row):
            if row == n:
                result.append( [ ''.join(board[i]) for i in range(n) ])
                return
            
            for col in range(n):
                if emptyCol[col] and empty45[row+col] and empty135[n-1+col-row]:
                    emptyCol[col], empty45[row+col], empty135[n-1+col-row] = False, False, False
                    board[row][col] = 'Q'
                    backTracking(row+1)
                    emptyCol[col], empty45[row+col], empty135[n-1+col-row] = True, True, True
                    board[row][col] = '.'

        return result


s=Solution()
print(s.solveNQueens(4))
