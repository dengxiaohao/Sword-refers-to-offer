'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读
取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

class Solution:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,data):
        # write code here
        length=len(self.data)
        if length%2==0:
            return (self.data[length//2]+self.data[length//2-1])/2.0
        else:
            return self.data[int(length//2)]