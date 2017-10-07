class MedianFinder(object):
    def kInversePairs(self, nums, k):
        P=[0]
        ma=0
        for x in nums:
            P.append(P[-1]+x)
            
        for i in range(len(nums)-k+1):
            diff=P[i+k]-P[i]
            ma=max(ma,diff)
        return ma/float(k)

    
s=MedianFinder()
print(s.kInversePairs([1,12,-5,-6,50,3],4))
