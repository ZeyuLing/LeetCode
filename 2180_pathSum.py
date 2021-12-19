# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        if root is None: return []
        self.result=[]
        self.target=target
        self.dfs(root,root.val,[root.val])
        return self.result
    def dfs(self,cur_node,cur_sum,cur_path):
        if cur_node.left is None and cur_node.right is None:
            if cur_sum==self.target: self.result.append(cur_path)
            return
        if cur_node.left is not None:
            new_path=copy(cur_path)
            new_path.append(cur_node.left.val)
            self.dfs(cur_node.left,cur_sum+cur_node.left.val,new_path)
        if cur_node.right is not None:
            new_path=copy(cur_path)
            new_path.append(cur_node.right.val)
            self.dfs(cur_node.right,cur_sum+cur_node.right.val,new_path)
