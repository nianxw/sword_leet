"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
"""

# 核心思想：当弹出的时候，判断s2栈中是否有元素，如果没有，则应把s1中的元素全部弹出压入s2中，
# 有元素的话，直接弹出即可

class CQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.s1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.s2 == []:
            if self.s1 == []:
                return -1
            while self.s1 != []:
                self.s2.append(self.s1.pop())
        return self.s2.pop()