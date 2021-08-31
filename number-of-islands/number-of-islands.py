def dfs(grid, x, y):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '0':
            return 0
        grid[y][x] = '0'
        dfs(grid, x, y + 1)
        dfs(grid, x, y - 1)
        dfs(grid, x + 1, y)
        dfs(grid, x - 1, y)
        return 1

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    islands += dfs(grid, x, y)
        return islands