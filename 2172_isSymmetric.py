# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import copy


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None :
            return True
        clone_root=self.clone(root)
        mirror=self.mirrorTree(clone_root)
        return self.comp(mirror,root)
    def clone(self,root):
        clone_root=copy(root)
        if root.left is not None:
            clone_root.left=self.clone(root.left)
        if root.right is not None:
            clone_root.right=self.clone(root.right)
        return clone_root
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        self.swap(root)
        return root
    def swap(self,node):
        if(node.left is not None):
            self.swap(node.left)
        if(node.right is not None):
            self.swap(node.right)
        if node.left is not None or node.right is not None:
            temp=node.left
            node.left=node.right
            node.right=temp
    def comp(self,A,B):
        if A is None and B is None :return True
        if (A is None and B is not None) or (A is not None and B is None):return False
        if A.val != B.val : return False
        if not self.comp(A.left,B.left): return False
        if not self.comp(A.right,B.right): return False
        return True
