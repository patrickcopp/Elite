class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        high = 0
        print(type(matrix[0][0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i - 1 >= 0 and j - 1 >= 0:
                    print(i,j)
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1],matrix[i - 1][j - 1]) + 1
                high = max(matrix[i][j], high)
        return high **2
                    
        