'''输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")