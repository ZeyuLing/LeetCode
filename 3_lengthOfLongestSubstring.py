class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX=-1
        if(len(s)<=1):return len(s)
        for i in range(len(s)):
            cur_substr=s[i:i+1]
            for j in range(i+1,len(s)):
                repeat=False
                #判断当前字母是否与前面的字母重复
                if(s[j] in cur_substr):     #重复就到重复字母下表+1位置
                    i+=cur_substr.index(s[j])
                    break
                #不重复就扩大subctr
                cur_substr=s[i:j+1]
            if (len(cur_substr) > MAX):
                MAX = len(cur_substr)
        return MAX
