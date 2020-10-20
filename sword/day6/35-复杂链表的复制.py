'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
'''


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur = head
        # 先拷贝next
        while cur:
            node = Node(cur.val)
            tmp = cur.next
            cur.next = node
            cur.next.next = tmp
            cur = tmp

        # 拷贝random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next

        old_node = head
        new_node = head.next
        res_node = head.next
        while old_node:
            old_node.next = old_node.next.next
            old_node = old_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            new_node = new_node.next
        return res_node

