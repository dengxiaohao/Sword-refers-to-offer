'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最
小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])