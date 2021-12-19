import numpy as np
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        visit=np.zeros(shape=[m,n],dtype=int)
        self.dfs(0,0,m,n,k,visit)
        return np.sum(visit)
    def dfs(self,x,y,m,n,k,visit):
        sum=0
        for char in str(x):
            sum+=int(char)
        for char in str(y):
            sum+=int(char)
        if(sum>k): return
        visit[x,y]=1
        neighbor_list=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for neighbor in neighbor_list:
            n_x,n_y=neighbor
            if(n_x>=0 and n_x<m and n_y>=0 and n_y<n and visit[n_x,n_y]==0):
                self.dfs(n_x,n_y,m,n,k,visit)
