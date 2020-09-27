"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""


def reversePrint1(head):
    if head is None:
        return []
    res = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    return res[::-1]


def reversePrint2(head):
    if head is None:
        return []
    return reversePrint2(head.next).append(head.val)