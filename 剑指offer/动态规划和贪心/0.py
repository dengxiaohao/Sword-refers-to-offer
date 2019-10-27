'''
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
'''

class Solution:
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        x = number % 3
        y = number // 3
        if x == 0:
            return 3**y 
        if x == 1:
            return 4 * 3**(y-1)
        else:
            return 2 * 3**y 