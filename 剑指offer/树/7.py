'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）
中，按结点数值大小顺序第三小结点的值为4。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k<1:
            return None
        stack = []
        res = []
        while pRoot or stack:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop()
            res.append(pRoot)
            pRoot = pRoot.right
        if len(res)<k:
            return None
        return res[k-1]