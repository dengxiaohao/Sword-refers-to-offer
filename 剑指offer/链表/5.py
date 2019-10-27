'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空
'''
class RandomListNode:
    def __init__(self, x):
    self.label = x
    self.next = None
    self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        head = pHead
        p_head = None
        new_head = None
        random_dic = {}
        old_new_dic = {}
        while head:
            node = RandomListNode(head.label)
            node.random = head.random
            old_new_dic[id(head)] = id(node)
            random_dic[id(node)] = node
            head = head.next
            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node
        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head