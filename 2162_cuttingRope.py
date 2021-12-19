import numpy as np
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        #任何大于3的数字都能拆成2和3的组合
        if n<=3 : return n-1
        res=1
        #大于5的数 分解出最多个3

        while(n>=5):
            res*=3
            res%=(1e9+7)
            n-=3
        #  1 2 3 4 的最大积都是自己 直接乘
        res=int(int(res*n)%(1e9+7))

        return res