class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0 
        right=len(height)-1

        max_left=max_right=res=0

        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=max_left:
                    max_left=height[left]
                else:
                    res+=max_left-height[left]
                left+=1

            else:
                if height[right]>=max_right:
                    max_right=height[right]
                else:
                    res+=max_right-height[right]
                right-=1           
        return res

s=Solution()
print(s.trap([0,1,0,2,1,0,1,3]))
