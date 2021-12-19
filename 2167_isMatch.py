import numpy as np


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = np.zeros(shape=[n + 1, m + 1], dtype=int)
        for i in range(n + 1):
            for j in range(m + 1):
                if j == 0:
                    if i == 0:  # 如果正则式已经空了 那s也得为空 否则不匹配
                        dp[i, j] = 1
                else:
                    if p[j - 1] != '*':
                        if p[j - 1] == '.':  # 这一位肯定匹配 但.不能匹配空串
                            if i > 0 and j > 0:  # 非空
                                dp[i, j] = dp[i - 1, j - 1]
                        else:  # 普通字母
                            if i > 0 and p[j - 1] == s[i - 1]:  # s不为空 比较是否相同
                                dp[i, j] = dp[i - 1, j - 1]
                    else:
                        # dp[i,j-2]:*匹配0次
                        # dp[i-1,j]:*匹配1次 前提是s[i-1]=p[j-2]或p[j-2]为‘.' p[j-2]是循环字符
                        # 比较的前提是s不为空
                        if dp[i, j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1, j]):
                            dp[i, j] = 1
                        else:
                            dp[i, j] = 0

        if dp[n, m] == 1: return True
        return False
