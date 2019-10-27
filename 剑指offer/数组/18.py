'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:
    def reOrderArray(self, array):
        stack1 = []
        stack2 = []
        for i in range(len(array)):
            if array[i] % 2:
                stack1.append(array[i])
            else:
                stack2.append(array[i])
        lenth1 = len(stack1)
        lenth2 = len(stack2)
        for i in range(lenth1):
            array[i] = stack1.pop(0)
        for i in range(lenth1,lenth1+lenth2):
            array[i] = stack2.pop(0)
        return array