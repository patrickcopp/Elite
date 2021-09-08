# 0 = dead
# 1 = alive
# 2 = dead, going to be alive
# 3 = alive, going to be dead

def determine_state(x, y, board):
    neighbours = neighbour_count(x, y, board)
    if board[x][y] == 1:
        if neighbours < 2 or neighbours > 3:
            board[x][y] = 3
    else:
        if neighbours == 3:
            board[x][y] = 2
    
def neighbour_count(x, y, board):
    total = 0
    neighbours = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
    for x_plus,y_plus in neighbours:
        if 0 <= x + x_plus < len(board) and 0 <= y + y_plus < len(board[0]) and board[x + x_plus][y + y_plus] % 2 == 1:
            total += 1
    return total

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                determine_state(i,j,board)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 2:
                    board[x][y] = 1
                if board[x][y] == 3:
                    board[x][y] = 0
        
        