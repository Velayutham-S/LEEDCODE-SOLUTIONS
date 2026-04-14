class Solution:
    def isToeplitzMatrix(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True