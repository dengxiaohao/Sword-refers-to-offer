'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k < 1:
            return None
        p = head
        q = head
        while k >= 1:
            if q:
                q = q.next
                k -= 1
            else:
                return None
        while q:
            q = q.next
            p = p.next
        return p