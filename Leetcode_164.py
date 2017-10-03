import math
class Solution(object):
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        imin = min(num)
        imax = max(num)
        gap = int( math.ceil( float(imax - imin)/(len(num)-1) ) )
        print(gap)
        # actually needed bucket numbers, reduce useless bucket
        bucketNum = int( math.ceil(float(imax - imin)/gap ) )
        bucketMin = [2147483647]* bucketNum
        bucketMax = [0]* bucketNum
        print(bucketNum)
        for i in num:
            if i == imin or i == imax:
                continue
            idx = (i - imin)/ gap
            bucketMin[idx] = min(bucketMin[idx], i)
            bucketMax[idx] = max(bucketMax[idx], i)
        print(bucketMin)
        print(bucketMax)
        maxgap = 0
        # consider min
        previous = imin
        for i in range(bucketNum):
            if bucketMin[i] == 2147483647 and bucketMax[i] == 0:
                #empty bucket
                continue
            maxgap = max(maxgap, bucketMin[i] - previous)
            previous = bucketMax[i]
        #consider max
        maxgap = max(maxgap, imax - previous)
        return maxgap



s=Solution()
print(s.maximumGap([1,2,3,10]))
