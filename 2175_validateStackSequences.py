class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        cur_in=0 # 已经进栈的节点数 也表示下一个要进栈的元素是pushed[cur_in]
        index_map={}
        #记录每个元素的进栈序号
        for index,val in enumerate(pushed):
            index_map[val]=index
        stack=[]
        for pop in popped:
            if(index_map[pop]>=cur_in):
                for i in range(cur_in,index_map[pop]+1):      #该在pop前进栈的元素全部进栈，并把pop出栈
                    stack.append(pushed[cur_in])
                    cur_in+=1
                stack.pop()
            elif pop==stack[-1]:       #当前元素已经在栈里了 那他必须是栈顶元素
                stack.pop()
            else:           #当前元素想要出栈 但他不再栈顶
                return False
        return True



