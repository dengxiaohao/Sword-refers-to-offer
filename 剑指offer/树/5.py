'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        temp = [pRoot]
        while temp:
            lenth = len(temp)
            val = []
            for i in range(lenth):
                p = temp.pop(0)
                val.append(p.val)
                if p.left:
                    temp.append(p.left)
                if p.right:
                    temp.append(p.right)
            res.append(val)
        return res