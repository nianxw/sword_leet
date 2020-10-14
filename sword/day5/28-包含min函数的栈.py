'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if self.min_data:
            if x < self.min_data[-1]:
                self.min_data.append(x)
            else:
                self.min_data.append(self.min_data[-1])
        else:
            self.min_data.append(x)



    def pop(self):
        """
        :rtype: None
        """
        self.min_data.pop()
        self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()