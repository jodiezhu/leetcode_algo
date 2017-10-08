class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            drop=len(nums)-k #kick out numbers, if filled then stop kicking.
            out=[]
            for num in nums:
                while drop and out and out[-1]<num: #need to compare all item in the nums,==>while
                    out.pop() #remove the original item
                    drop-=1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a,b).pop(0) for _ in range(k)]
            
        return max(merge(prep(nums1,i),prep(nums2,k-i)) 
                   for i in range(k+1) 
                   if i<=len(nums1) and (k-i)<=len(nums2))


        #return 

s=Solution()
print(s.maxNumber([3,4,6,5,7,2,1],[9,2,3,4],4))  
