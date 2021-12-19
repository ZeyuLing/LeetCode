# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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
        temp=None
        if node.left is not None or node.right is not None:
            temp=node.left
            node.left=node.right
            node.right=temp

