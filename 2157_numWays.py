class Solution(object):
    # def numWays(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     #将n拆成若干个2和若干个1之和
    #     if(n==0 or n==1):return 1
    #     ways=0
    #     for num_2steps in range(int(n/2)+1):
    #         times=num_2steps+n-2*num_2steps     #跳的次数
    #         #times次里选num_2steps一次跳2阶 n-2*num_2steps 次一次跳1阶
    #         ways+=int(self.C(times,min(num_2steps,n-2*num_2steps))%(1e9+7))
    #     return int(ways%(1e9+7))
    # def C(self,n,m):
    #     return self.factorial(n)/(self.factorial(m)*self.factorial(n-m))
    # def factorial(self,n):
    #     if(n==0):return 1
    #     result=1
    #     for i in range(1,n+1):
    #         result*=i
    #     return result
    def numWays(self, n):       #斐波那契法
        """
        :type n: int
        :rtype: int
        """
        #跳到第n阶的方法数为：
            #调到第n-1阶的方法数+
            #跳到第n-2阶的方法数
        ways_list=[]
        for i in range(0,n+1):
            if(i==0 or i==1):ways_list.append(1)
            else:ways_list.append(int(ways_list[i-1]%(1e9+7))+int(ways_list[i-2]%(1e9+7)))
        return int(ways_list[n]%(1e9+7))
