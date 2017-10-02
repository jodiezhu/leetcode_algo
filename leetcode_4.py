'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

#Median of 2 sorted array
class Solution(object):
    def splitArray(self, A, B):
        m,n=len(A),len(B)

        if m>n:
            m,n,A,B=n,m,B,A

        imin,imax=0,m

        while imin<=imax:
            i=int((imin+imax)/2)
            j=int((m+n+1)/2-i)

            if i<m and A[i]<B[j-1]:imin=i+1
            elif i>0 and B[j]<A[i-1]:imax=i-1

            else:
                if i==0: max_left=B[j-1]
                if j==0: max_left=A[i-1]
                if i==m: min_right=B[j]
                if j==n: min_right=A[i]
                
                else:
                    max_left=max(A[i-1],B[j-1])
                    min_right=min(A[i],B[j])

                if (m+n)%2==1:
                    return max_left
                else:
                    return (max_left+min_right)/2


s=Solution()
print(s.splitArray([2,5,10,18],[1,1,7]))