'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k == 0:
            return []
        if k > len(tinput):
            return []
        l = 0
        r = len(tinput) - 1
        pivod = self.partation(tinput,l,r)
        while pivod > k-1:
            r = pivod-1
            pivod = self.partation(tinput,l,r)
        while pivod < k-1:
            l = pivod+1
            pivod = self.partation(tinput,l,r)
        res = sorted(tinput[:k])
        return res
    def partation(self,tinput,l,r):
        p = l-1
        for i in range(l,r):
            if tinput[i] < tinput[r]:
                p += 1
                tinput[i],tinput[p] = tinput[p],tinput[i]
        tinput[p+1],tinput[r] = tinput[r],tinput[p+1]
        return p+1