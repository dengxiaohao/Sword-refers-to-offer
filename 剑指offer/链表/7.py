'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        megerhead = ListNode(0)
        p = megerhead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                megerhead.next = pHead1
                pHead1 = pHead1.next
            else:
                megerhead.next = pHead2
                pHead2 = pHead2.next
            megerhead = megerhead.next
        if pHead1:
            megerhead.next = pHead1
        if pHead2:
            megerhead.next = pHead2
        return p.next