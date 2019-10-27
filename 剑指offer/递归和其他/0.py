'''题目'''
'''大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if 0<n<3:
            return 1
        res = []
        res.append(1)
        res.append(1)
        for i in range(2,n):
            res.append(res[i-1]+res[i-2])
        return res[-1]