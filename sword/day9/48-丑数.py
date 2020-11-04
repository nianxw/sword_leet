'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。
求按从小到大的顺序的第 n 个丑数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:

1 是丑数。
n 不超过1690。
'''

# 这道题相当于是对三个有序数组进行排序，丑数数组*2， 丑数数组*3， 丑数数组*5


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1 for _ in range(n)]  # res中记录的是前n个丑数的值
        i, j, k = 0, 0, 0  # i, j, k分别代表三个指针，指向有序数组对应位置
        for m in range(1, n):
            res[m] = min(res[i]*2, res[j]*3, res[k]*5)  # 比较排序数组值的大小

            if res[m] == res[i]*2:   # 谁小，谁的指针就向后移动
                i += 1
            if res[m] == res[j]*3:   # 这里有三个if是为了去重
                j += 1
            if res[m] == res[k]*5:
                k += 1

        # 这里也不会出现指针超过当前res中存储的丑数数目，因为每次res都会+1个丑数，而i,j,k也是最多+1
        return res[n-1]