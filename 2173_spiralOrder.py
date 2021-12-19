import numpy as np
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(matrix==[]):return []
        result=[]
        matrix=np.array(matrix,dtype=int)
        lb=0
        rb=matrix.shape[1]-1
        ub=0
        db=matrix.shape[0]-1
        while 1:
            if (lb > rb or ub > db): break
            for i in range(lb,rb+1):
                result.append(matrix[ub,i])
            ub+=1
            if (lb > rb or ub > db): break
            for i in range(ub,db+1):
                result.append(matrix[i,rb])
            rb-=1
            if (lb > rb or ub > db): break
            for i in range(rb,lb-1,-1):
                result.append(matrix[db,i])
            db-=1
            if (lb > rb or ub > db): break
            for i in range(db,ub-1,-1):
                result.append(matrix[i,lb])
            lb+=1
        return result

