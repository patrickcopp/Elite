class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(x, y, ocean):
            if (x,y) in ocean:
                return
            ocean.add((x, y))
            if x > 0 and heights[x - 1][y] >= heights[x][y]:
                dfs(x - 1, y, ocean)
            if x < len(heights) - 1 and heights[x + 1][y] >= heights[x][y]:
                dfs(x + 1, y, ocean)
            if y > 0 and heights[x][y - 1] >= heights[x][y]:
                dfs(x, y - 1, ocean)
            if y < len(heights[0]) - 1 and heights[x][y + 1] >= heights[x][y]:
                dfs(x, y + 1, ocean)
            
        pacific = set()
        atlantic = set()
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights) - 1, i, atlantic)
            
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)
            
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atlantic and (i, j) in pacific:
                    res.append([i,j])
        return res
        