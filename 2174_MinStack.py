class Node(object):
    def __init__(self,x):
        self.MIN=1e10
        self.val=x
class MinStack(object):

    def __init__(self):
        self.stack=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node=Node(x)
        if(len(self.stack)==0 or x<=self.stack[-1].MIN):
            node.MIN=x
        else:
            node.MIN=self.stack[-1].MIN
        self.stack.append(node)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val


    def min(self):
        """
        :rtype: int
        """
        return self.stack[-1].MIN


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()