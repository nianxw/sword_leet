'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
'''


# B 的结果是两个三角矩阵拼接而成

'''

1       a[1]        a[2]        a[3]
a[0]    1           a[2]        a[3]
a[0]    a[1]        1           a[3]
a[0]    a[1]        a[2]        1

'''


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        res = [1]*len(a)
        tmp = 1
        for i in range(1, len(a)):
            res[i] = res[i-1] * a[i-1]
        for j in range(len(a)-2, -1, -1):
            tmp *= a[j+1]
            res[j] *= tmp
        return res