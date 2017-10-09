##Method 1: Navie Solution, Time: O(n^2), Space: O(n)
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        sums=[0]*(len(nums)+1)
        ans=0
        
        for i in range(len(nums)):
          sums[i+1]=sums[i]+nums[i]
          
        for i in range(len(nums)):
          for j in range(i+1,len(nums)+1):
            if sums[j]-sums[i]>=lower and sums[j]-sums[i]<=upper:
              ans+=1
        return ans
