class stack:
    def __init__(self):
        self.item = []

    def push(self,x):
        self.item.append(x)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def empty(self):
        return self.item == []

    def size(self):
        return len(self.item)


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = stack()
        self.stack2 = stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2.size() <= 0:
            while self.stack1.size() > 0:
                data = self.stack1.peek()
                self.stack1.pop()
                self.stack2.push(data)
        if self.stack2.size() == 0:
            print("empty queue")
            return -1
        result = self.stack2.peek()
        self.stack2.pop()
        return result



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2.size() <= 0:
            while self.stack1.size() > 0:
                data = self.stack1.peek()
                self.stack1.pop()
                self.stack2.push(data)
        if self.stack2.size() == 0:
            print("empty queue")
            return -1
        result = self.stack2.peek()
        return result

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1.size() == 0 and self.stack2.size() == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()