import numpy as np
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=-9999999
        for i in range(len(s)):
            count=0
            while((i+count+1)<len(s) and s[i+count+1]==s[i]):
                count+=1
            if((count+1)>max):max=count+1
            i+=count
        return max


