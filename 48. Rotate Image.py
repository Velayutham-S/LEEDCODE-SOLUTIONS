class Solution:
    def rotate(self, matrix):
        list1 = []
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
            matrix[i].reverse()

        