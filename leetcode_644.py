class MedianFinder(object):
    def findMax(self, nums, k):
        max_val=max(nums)
        min_val=min(nums)
        prev_mid=max_val #random assign for the initial to start with
        error=max_val

        while abs(error)>0.000001:
            mid=float((max_val+min_val)/2)
            if self.check(nums,mid,k):
                min_val=mid
                
            else:
                max_val=mid

            error=prev_mid-mid
            prev_mid=mid

        return mid
    
    def check(self,nums,mid,k):
        sum,prev,min_sum=0,0,0
        
        for i in range(k):
            sum+=nums[i]-mid
                     
        if sum>=0:
            return True
            
        for i in range(k,len(nums)):
            sum += nums[i]-mid
            prev+= nums[i-k]-mid
            min_sum=min(prev,min_sum)
            if sum>=min_sum:
                return True
        
        return False
        
    
s=MedianFinder()
print(s.findMax([1,12,-5,-6,50,3],4)) 
