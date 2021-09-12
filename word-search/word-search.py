class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, word, visited):
            if 0 > x or x >= len(board) or 0 > y or y >= len(board[0]):
                return False
            if board[x][y] != word[0]:
                return False
            if (x,y) in visited and visited[(x,y)]:
                return False
            if len(word) == 1:
                return True
            visited[(x,y)] = True
            if dfs(x + 1, y, word[1:], visited) or dfs(x - 1, y, word[1:], visited) or dfs(x, y + 1, word[1:], visited) or dfs(x, y - 1, word[1:], visited):
                return True
            visited[(x,y)] = False
            return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and (word == board[i][j] or dfs(i, j, word, {})):
                    return True
        return False