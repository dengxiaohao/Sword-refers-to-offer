'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''


class Solution:
    stack = []
    stackmin = []
    def push(self, node):
        self.stack.append(node)
        if not self.stackmin or self.stackmin[-1] >= self.stack[-1]:
            self.stackmin.append(self.stack[-1])
    def pop(self):
        if self.stack[-1] == self.stackmin[-1]:
            self.stackmin.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.stackmin[-1]