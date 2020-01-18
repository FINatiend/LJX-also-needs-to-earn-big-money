class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # print(len(self.queue2))
        if len(self.queue1)!=0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
            print(len(self.queue2))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return -1
        if len(self.queue1) == 0:
             while len(self.queue2) > 1:
                 data = self.queue2.pop(0)
                 self.queue1.append(data)
             return self.queue2.pop()
        else:
            while len(self.queue1) > 1:
                data = self.queue1.pop(0)
                self.queue2.append(data)
            return self.queue1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return -1
        if len(self.queue1) == 0:
             while len(self.queue2) > 0:
                 data = self.queue2.pop(0)
                 self.queue1.append(data)
             return data
        else:
            while len(self.queue1) > 0:
                data = self.queue1.pop(0)
                self.queue2.append(data)
            return data

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)