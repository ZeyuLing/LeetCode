import numpy as np
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board=np.array(board)
        #
        start_location=[]       #起始位置
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if(board[i,j]==word[0]):
                    start_location.append([i,j])
        for location in start_location:
            visit=np.zeros(shape=board.shape,dtype=np.int)  #存储是否访问过
            x,y=location       #记录当前坐标
            flag_found=self.dfs(location,1,board,word,visit)
            if(flag_found):return True
        return False




    def dfs(self,cur_location,cur_index,board,word,visit):
        #cur_location,当前位置
        #cur_index 当前要搜索的字母的下表
        if(cur_index>=len(word)):return True
        x,y=cur_location
        visit[x,y]=1
        neighbor_list = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]  # 邻接节点
        for neighbor in neighbor_list:
            if (self.check(neighbor, board.shape) and (visit[neighbor[0], neighbor[1]] == 0)):
                if (board[neighbor[0], neighbor[1]] == word[cur_index]):  # 如果找到该字母
                    flag_found=self.dfs(neighbor,cur_index+1,board,word,visit.copy())
                    #这里必须传copy 否则错误的路径探索也会修改visit的值
                    if(flag_found) : return True
        return False


    def check(self,location,shape):
        if(location[0]>=0 and location[0]<shape[0]):
            if(location[1]>=0 and location[1]<shape[1]):
                return True
        return False