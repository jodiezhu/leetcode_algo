from collections import deque #deque:list-like container with fast appends and pops on either end

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        
        res=[]
        dq=deque()
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i>k-2:
                res.append(nums[dq[0]])
        return res
        
 
s=Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
