class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self,node):
        self.stack.append(node)

        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            # 为了保证一个任一个出栈后最小栈也有一个出栈，切最小栈的栈顶仍然为最小的值，
            # 这里要进行一个else判断将当前的最小值复制一个
            self.minstack.append(self.min())

    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None

        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]
