'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        lo,hi=0,n-1

        while lo<hi:
            mid=int((hi-lo)/2+lo)

            if (nums[mid]>nums[hi]):
                lo=mid+1
            elif nums[mid]<nums[hi]:
                hi=mid
            else: #nums[mid]=nums[hi]
                hi-=1 #we couldn't sure the position of minimum in mid's left or right, so just let upper bound reduce one

        return nums[lo]


s=Solution()
print(s.findMin([1,1]))
