'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        def sam(root1,root2):
            if not root1 and not root2:
                return True
            if (root1 and root2) and root1.val == root2.val:
                return sam(root1.left,root2.right) and sam(root1.right,root2.left)
            return False
        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if pRoot.right and not pRoot.left:
            return False
        return sam(pRoot.left,pRoot.right)