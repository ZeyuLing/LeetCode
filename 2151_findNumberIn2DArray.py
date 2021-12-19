import numpy as np
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(matrix==[]) :return False
        n=len(matrix)   #行
        m=len(matrix[0])   #列
        np_matrix=np.array(matrix)
        if(n>m):
            for i in range(m):      #遍历每一列
                if(target in np_matrix[:,i]): return True
        else :
            for i in range(n):      #遍历每一行
                print(matrix[i])
                if(target in np_matrix[i,:]):return True
        return False
s=Solution()
s.findNumberIn2DArray([[5],[6]],5)