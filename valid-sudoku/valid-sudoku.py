class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != '.':
                            if board[i * 3 + k][j * 3 + l] not in box:
                                box.add(board[i * 3 + k][j * 3 + l])
                            else:
                                return False
        for i in range(9):
            vline = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in vline:
                        vline.add(board[j][i])
                    else:
                        return False
                    
        for i in range(9):
            hline = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in hline:
                        hline.add(board[i][j])
                    else:
                        return False
        return True
        