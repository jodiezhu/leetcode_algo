'''
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
'''

#Smallest Range
class Solution(object):
    def smallestRange(self, A): #A:[[1,4,7],[2,3,9,11],[5,6,8]]
        ans=-1e9, 1e9
        
        for right in sorted(set(x for l in A for x in l))[::-1]:
            
            for B in A:
                while B and right<B[-1]:
                    B.pop()
                if not B:
                    return ans
            
            
            left=min(B[-1] for B in A)
            
            if right-left<=ans[1]-ans[0]:
                ans=left,right
                
        return ans

s=Solution()
print(s.smallestRange([[24,26],[20],[22,30]]))