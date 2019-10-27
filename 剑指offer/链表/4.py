'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree

        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right

        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left