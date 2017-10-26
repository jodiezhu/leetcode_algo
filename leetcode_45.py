class Solution:
    def jump(self, A):
        if len(A)<=1:
            return 1
        
        step,max_range,next_range=1,A[0],A[0]

        for i in range(1,len(A)):
            if max_range>=len(A)-1:
                return step
            if i>max_range:
                max_range=next_range
                step+=1
            next_range=max(next_range,i+A[i])
        return step


s=Solution()
print(s.jump([2,3,1,1,4]))
