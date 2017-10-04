import math
class Solution(object):
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        imin = min(num)
        imax = max(num)
        
        if imin==imax: return 0 #another special case to avoid gap=0
        
        gap = int( math.ceil( float(imax - imin)/(len(num)-1) ) )
        print(gap)
        
        # actually needed bucket numbers, reduce useless bucket
        bucketNum = int( math.ceil(float(imax - imin)/gap ) )
        bucketMin = [2**31-1]* bucketNum #save min in each bucket
        bucketMax = [0]* bucketNum #save max
 
        for i in num:
            if i == imin or i == imax:
                continue
            idx = (i - imin)/ gap #decide which bucket to stay
            bucketMin[idx] = min(bucketMin[idx], i)
            bucketMax[idx] = max(bucketMax[idx], i)

        maxgap = 0
        # consider min
        previous = imin
        for i in range(bucketNum):
            if bucketMin[i] == 2**31-1 and bucketMax[i] == 0:
                #empty bucket
                continue
            maxgap = max(maxgap, bucketMin[i] - previous)
            previous = bucketMax[i]
        #consider max
        maxgap = max(maxgap, imax - previous) #previous=the last bucket max
        return maxgap



s=Solution()
print(s.maximumGap([1,1,1,1]))
