'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

class Solution:
    def EntryNodeOfLoop(self, pHead):
        lst = list()
        while pHead:
            if pHead not in lst:
                lst.append(pHead)
                pHead = pHead.next
            else:
                return pHead
        return None