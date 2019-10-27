'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        new_head = ListNode(0)
        new_head.next = pHead
        pre = new_head
        last = new_head.next
        while last:
            if last.next and last.val == last.next.val:
                while last.next and last.val == last.next.val:
                    last = last.next
                pre.next = last.next
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return new_head.next