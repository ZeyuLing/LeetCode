import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s)==1): return s
        MAX_radius=-1
        MAX=-1
        final_pivot=0
        for double_pivot in range(2*len(s)):
            pivot=1.0*double_pivot/2
            radius=0
            if((math.ceil(pivot+radius)>=len(s))or (int(pivot-radius)<0)):break
            while(math.ceil(pivot + radius) < len(s))and (int(pivot - radius) >= 0):
                if(s[int(math.ceil(pivot+radius))]!=s[int(pivot - radius)]):
                    break
                if MAX < int(math.ceil(pivot + radius)) - int(pivot - radius):
                    MAX = int(math.ceil(pivot + radius)) - int(pivot - radius)
                    final_pivot = pivot
                    MAX_radius = radius
                radius+=1
        return s[int(final_pivot-MAX_radius):int(math.ceil(final_pivot+MAX_radius))+1]