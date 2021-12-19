import numpy as np
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        recorder=np.zeros(shape=100000,dtype=np.int)
        for number in nums:
            recorder[number]+=1
            if(recorder[number]>1):
                return number
