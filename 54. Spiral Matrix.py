class Solution:
    def spiralOrder(self, matrix):
        list1 = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        final = (right+1) * (bottom+1)
        for i in range(0,len(matrix)):  
            for j in range(i,right+1):
                list1.append(matrix[left][j])
            top = j
            left+=1
            for k in range(left,bottom+1):
                list1.append(matrix[k][top])
            right-=1
            for z in range(right,i-1,-1):
                list1.append(matrix[bottom][z])
            for x in range(bottom-1,i,-1):
                if i < len(matrix[i]):
                    list1.append(matrix[x][i])
            bottom-=1
        return list1[:final]
        