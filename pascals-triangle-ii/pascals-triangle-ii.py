class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [0,1,0]
        for i in range(rowIndex):
            temp = [0]
            for i in range(len(triangle) - 1):
                temp.append(triangle[i] + triangle[i+1])
            temp.append(0)
            triangle = temp
            print(triangle)
        return triangle[1:-1]