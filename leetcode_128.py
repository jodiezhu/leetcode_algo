'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

'''

class Solution(object):
    def longestConsecutive(self, nums):
        A=set(nums)
        best=0
        for x in A:
            if x-1 not in A:
                y=x+1
                while y in nums:
                    y+=1
                best=max(best,y-x)
        return best


s=Solution()
print(s.longestConsecutive([2,4,1,1,3,8,9,1]))
