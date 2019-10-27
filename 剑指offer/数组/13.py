'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


class Solution:
    def multiply(self, A):
        if not A:
            return []
        num = len(A)
        B = [None] * num
        B[0] = 1
        for i in range(1, num):
            B[i] = B[i-1] * A[i-1]
        tmp = 1
        for i in range(num-2, -1, -1):
            tmp *= A[i+1]   
            B[i] *= tmp
        return B