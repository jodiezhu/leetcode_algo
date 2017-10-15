'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

'''
#Method 1: Binary Search
class Solution(object):
    def countSmaller(self, nums):
        sorted=[]
        ans=[0]*len(nums)

        for i in range(len(nums))[::-1]:
            index=self.findIndex(sorted,nums[i])
            ans[i]=index
            sorted.insert(index,nums[i]) ##Using insert!!!!!!
        return ans

    def findIndex(self,sorted,target):

        start=0
        end=len(sorted)-1
        #all special cases:
        if len(sorted)==0: return 0
        if sorted[end]<target: return end+1
        if sorted[start]>=target: return 0

        while start<end:
            mid=int(start+(end-start)/2)
            if sorted[mid]<target:
                start=mid+1
            else:
                end=mid
        return start

'''
#second way of findIndex
def findIndex(self,sorted,target):

        start=0
        end=len(sorted)-1

        if len(sorted)==0: return 0

        while start<=end:
            mid=int(start+(end-start)/2)
            if sorted[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return start

'''
'''
#Method 2:Recurrsive: Mergesort
def countSmaller(nums):
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)),smaller)
    return smaller

        
def sort(enum,smaller):
    half = len(enum) / 2
    if half:
        left, right = sort(enum[:half],smaller), sort(enum[half:],smaller)
        for i in range(len(enum))[::-1]:
            print(left,right)
            if not right or left and left[-1][1] > right[-1][1]:
                smaller[left[-1][0]] += len(right)
                enum[i] = left.pop()
            else:
                enum[i] = right.pop()
            print(left,right)
    return enum
        


print(countSmaller([5,2,6,1]))
'''


s=Solution()
print(s.countSmaller([5,2,6,1]))
