'''
Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.
Example 1:
Input: 9
Output: 10
'''
#Remove 9
class Solution(object):
    def newinteger(self,n):
        ans=0
        base=1

        while n:
            ans+= n % 9 * base
            n=int(n/9)
            base*=10

        return ans

s=Solution()
print(s.newinteger(18))