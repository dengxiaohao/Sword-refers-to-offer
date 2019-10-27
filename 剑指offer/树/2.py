'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return pNode
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        while pNode.next:
            if pNode == pNode.next.left:
                return pNode.next
            else:
                pNode = pNode.next