'''
输入两个链表，找出它们的第一个公共节点。
注意：

.如果两个链表没有交点，返回 null.
.在返回结果后，两个链表仍须保持原有的结构。
.可假定整个链表结构中没有循环。
.程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# 不能改变原链表
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        a = headA
        len_a = 0
        while a != None:
            a = a.next
            len_a += 1
        b = headB
        len_b = 0
        while b != None:
            b = b.next
            len_b += 1

        a = headA
        b = headB
        while len_a < len_b:
            b = b.next
            len_a += 1

        while len_b < len_a:
            a = a.next
            len_b += 1
        
        while a!= None:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        return None
        