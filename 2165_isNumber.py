class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 大小写转换 两端去空格
        s = s.lower().strip(' ')
        # 不能有多个e
        count_e = s.count('e')
        if count_e > 1: return False
        nums = s.split('e')
        print(nums)
        for i, num in enumerate(nums):
            # 如果有e 则底数指数不能为空
            if (num == ''):
                if count_e == 1: return False
            if not self.checkPart(num, i):
                return False
        return True

    def checkPart(self, sub, is_ex):
        if sub == "":       #没有e且为空
            if (is_ex):
                return True
            else:
                return False
        count_dot = 0
        count_sign = 0
        hasNum= False
        for char in sub:
            # 不是数字字符
            if not (('0' <= char <= '9') or char == '.' or char == '+' or char == '-'):
                return False
            if char == '+' or char == '-':
                count_sign += 1
            if char == '.':
                count_dot += 1
            if (count_sign > 1): return False
            if (count_dot > 1): return False
            if '0' <= char <= '9':hasNum=True
        if not hasNum: return False  # 不能只有符号
        if is_ex:  # 指数部分 必须是整数
            if sub.count('.') >= 1: return False
        if count_sign == 1:  # 有符号必须是第一个 且不能只有符号
            if (sub[0] != '+' and sub[0] != '-') or len(sub)==1: return False


        return True
