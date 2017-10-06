'''
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur,sum =0,0
        for i in range(2,len(A)):
            if A[i-1]-A[i-2]==A[i]-A[i-1]:
                cur+=1
                sum+=cur
            else:cur=0

        return sum


s=Solution()
print(s.numberOfArithmeticSlices([2,4,6,8,10]))
