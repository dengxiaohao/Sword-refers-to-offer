'''
输入两个链表，找出它们的第一个公共结点。
'''

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        lst = list()
        while pHead1:
            lst.append(pHead1.val)
            pHead1 = pHead1.next

        while pHead2:
            if pHead2.val in lst:
                return pHead2
            pHead2 = pHead2.next
        return None