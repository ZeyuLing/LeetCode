class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        #搜索树inOrder有序
        inOrder=sorted(postorder)
        return self.verify(0,0,len(postorder),postorder,inOrder)

    def verify(self,post_head,in_head,len,postorder,inOrder):
        if len <=1 :return True
        root=postorder[post_head+len-1]     #当前子树的根节点
        bound=inOrder.index(root)       #中序中根节点的位置
        if(bound<0): return False   #没找到
        len_left=bound-in_head
        len_right=len-len_left-1
        #检查postorder中的左子树是不是都比根小 右子树都比根大
        for i in range(post_head,post_head+len_left):  #左子树要都比root小
            if postorder[i]>root: return False
        for i in range(post_head+len_left,post_head+len-1):
            if postorder[i]<root: return False

        return self.verify(post_head,in_head,len_left,postorder,inOrder) \
               and self.verify(post_head+len_left,bound+1,len_right,postorder,inOrder)