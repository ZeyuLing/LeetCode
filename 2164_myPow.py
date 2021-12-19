import math


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n==1):return x
        if(n==0):return 1
        if(n==-1): return 1/x
        #n是偶数 则转换成x^(n/2)的平方
        #n是奇数 则转换成 x*x^(n-1)
        if(n%2==0):
            half=self.myPow(x,int(n/2))
            return half*half
        else:
            return x*self.myPow(x,n-1)
