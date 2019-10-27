'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        lenth = len(sequence)
        if lenth == 0:
            return False
        if lenth == 1:
            return True
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        k = i 
        while sequence[i] > root:
            i += 1
        if i != lenth-1:
            return False
        treel = sequence[:k]
        treer = sequence[k:lenth-1]
        leftis = True
        rightis = True
        if treel:
            leftis = self.VerifySquenceOfBST(treel)
        if treer:
            rightis = self.VerifySquenceOfBST(treer)
        return leftis and rightis