'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        a=list()
        for i in range(len(array)):
            if array.count(array[i]) == 1:
                a.append(array[i])
        return a[0],a[1]