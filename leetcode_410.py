'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ? n ? 1000
1 ? m ? min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18
'''

class Solution(object):
    def splitArray(self, nums, m):
        l=max(nums)
        r=sum(nums)
        
        if m==1: return r

        while l<=r: 
            mid=(l+r)//2
            if self.validcheck(mid,nums,m):
                r=mid-1
            else:
                l=mid+1
        return l


    def validcheck(self,target,nums,m):
        count=1
        total=0
        for num in nums: 
            total+=num

            if total>target:
                total =num
                count+=1

                if count>m: 
                    return False

        return True


s=Solution()
print(s.splitArray([7,2,5,10,8],3))

##For example, we want to find the first number, which is larger or equal to a target value in a sorted array.
'''
int n=nums.length;
int l=0, r=n-1;
while(l<r){
     int mid=(r-l)/2+l;
     if(nums[mid]>=target){
            r=mid;
      }else{
            l=mid+1; 
      }
}
return nums[l]
'''
