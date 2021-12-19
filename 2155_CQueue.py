class CQueue(object):

    def __init__(self):
        self.queue=[]

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        return



    def deleteHead(self):
        """
        :rtype: int
        """
        if(len(self.queue)==0) :return -1
        return self.queue.pop(0)



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()