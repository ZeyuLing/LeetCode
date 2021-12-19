import numpy as np
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.MAX_list=-np.ones(shape=n+1,dtype=int)
        for i in range(1,n):
            self.dfs(i,i,n)
        return self.MAX_list[n]
    def dfs(self,cur_len,cur_mul,n):
        if(cur_mul>self.MAX_list[cur_len]):
            self.MAX_list[cur_len]=cur_mul
        elif cur_mul<self.MAX_list[cur_len]:
            return
        if(n==cur_len): return
        for i in range(1,n-cur_len+1):
            self.dfs(cur_len+i,cur_mul*i,n)
