# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None :return []
        queue=list()
        result=[]
        queue.append(root)
        while(len(queue)!=0):
            #每次把queue里所有元素的孩子都加入 并把父节点全都删除
            cur_level=queue
            queue=[]        #父节点全部出队
            #子节点全部入队
            for father in cur_level:
                if father.left is not None:
                    queue.append(father.left)
                if father.right is not None:
                    queue.append(father.right)
            tmp=[]
            for item in cur_level:
                tmp.append(item.val)
            result.append(tmp)
        return result
