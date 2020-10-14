'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            cur.next = ListNode(val)
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next