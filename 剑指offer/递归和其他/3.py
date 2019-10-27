'''我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法'''

class Solution:
    def rectCover(self, number):
        if number < 1:
            return 0
        p = q = r =0
        for i in range(1,number+1):
            if i == 1:
                p = q = r =1
            elif i == 2:
                q = r = 2
            else:
                r = q + p
                p = q
                q = r
        return r