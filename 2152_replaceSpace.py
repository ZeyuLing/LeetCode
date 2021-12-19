class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for char in s:
            if(char!=' '):result+=char
            else:result+='%20'
        return result