class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_2=bin(n)
        return str(n_2).count('1')
