# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if(preorder==[]) :return None
        tree_root=TreeNode(preorder[0])
        tree_root=self.createNodes(tree_root,0,0,len(preorder),preorder,inorder)
        return tree_root

    def createNodes(self,p,pre_head,in_head,len,preorder,inorder):
        if(len==0):return None
        if(p==None):
            p=TreeNode(preorder[pre_head])
        if(len==1):return p
        border=inorder.index(preorder[pre_head]) #找到根节点再inorder中的位置
        len_left=border-in_head
        len_right=len-len_left-1
        p.left= self.createNodes(p.left,pre_head+1,in_head,len_left,preorder,inorder)
        p.right=self.createNodes(p.right,pre_head+len_left+1,border+1,len_right,preorder,inorder)
        return p
s=Solution()
s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])