class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for num in nums:
            if(num%2):
                result.insert(0,num)
            else:
                result.append(num)
        return result