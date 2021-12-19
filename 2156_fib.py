class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_list=[]
        for i in range(n+1):
            if(i==0 or i==1):fib_list.append(i)
            else: fib_list.append(int((fib_list[i-1]+fib_list[i-2])%(1e9+7)))
        return fib_list[n]