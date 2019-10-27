'''
输入一个链表，反转链表后，输出新链表的表头。
'''

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None
        stack = [pHead.val]
        while pHead:
            pHead = pHead.next
            if pHead:
                stack.append(pHead.val)
        head = ListNode(stack.pop())
        Head = head
        while stack:
            Head.next = ListNode(stack.pop())
            Head = Head.next
        return head