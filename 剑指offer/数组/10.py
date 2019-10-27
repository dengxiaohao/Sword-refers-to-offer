'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有
1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可
以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n == 1:
            return 1
        res=0
        i = 1
        while i<=n:
            res += n//(10 * i)*i + min(max(n%(i*10)-i+1,0),i)
            i *= 10
        return res