##NOT DONE YET!!!!!!!!!
import heapq
class MedianFinder(object):
    def slidingMedian(self,nums,k):
        small,large,res=[],[],[0]*(len(nums)-k+1)
        
        for i in range(len(nums)):
            heapq.heappush(small, -heapq.heappushpop(large, nums[i]))
            if len(large) < len(small):
                heapq.heappush(large, -heapq.heappop(small))
  
            if len(large) + len(small)==k:
                if len(large) > len(small):
                    median= float(large[0])
                else:
                    median= float((large[0] - small[0]) / 2.0)
                
                start=i-k+1
                res[start]=median
                
                if (nums[start] in small):
                    small.remove(nums[start])
                elif (-nums[start] in small):
                    small.remove(-nums[start])
                else: large.remove(nums[start])

        return res
                

s=MedianFinder()
print(s.slidingMedian([1,3,-1,-3],3))    
