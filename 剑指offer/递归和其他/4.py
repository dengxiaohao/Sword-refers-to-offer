'''输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        res = []
        lenth = len(array)
        left = 0
        right = lenth-1
        while left <right:
            su = array[left] + array[right]
            if su == tsum:
                res.append(array[left])
                res.append(array[right])
                break
            elif su < tsum:
                left += 1
            else:
                right -= 1
        return res