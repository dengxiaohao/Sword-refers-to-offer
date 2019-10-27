'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.depth(pRoot.left) - self.depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def depth(self,root):
        if root == None:
            return 0
        nleft = self.depth(root.left)
        nright = self.depth(root.right)
        return max(nleft+1,nright+1)