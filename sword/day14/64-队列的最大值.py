'''
11.16

请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
'''
import queue

class MaxQueue(object):

    def __init__(self):
        self.deque = queue.deque()  # 双端单调队列
        self.queue = queue.Queue()

    def max_value(self):
        """
        :rtype: int
        """
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 这里应该是小于号，而不是小于等于
        # 原因在于对于相等的两个大数，双端队列中会存储两次，而不是只存储一次
        # 这样的话，当弹出头部大数时，不会影响到后面的最大值，否则双端队列就为空了
        # [1,2,5,4,5]  ----->  [1] --> [2] --> [5] --> [5,4] --> [5, 5]
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if self.queue.empty():
            return -1
        res = self.queue.get()
        if res == self.deque[0]:
            self.deque.popleft()
        return res
