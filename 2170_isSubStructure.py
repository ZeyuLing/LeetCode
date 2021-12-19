# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        return self.traverse(A,B)
    def traverse(self,node,sub):
        if node is None:
            return False
        if self.comp(node,sub):
            return True
        else:
            if node.left is not None:
                if self.traverse(node.left,sub):
                    return True
            if node.right is not None:
                if self.traverse(node.right,sub):
                    return True
        return False
    def comp(self,node,sub):
        if (node is None and sub is not None) or (node is not None and sub is None):
            return False
        if node.val!=sub.val:return False
        if sub.left is not None:
            if not self.comp(node.left,sub.left):
                return False
        if sub.right is not None:
            if not self.comp(node.right,sub.right):
                return False
        return True