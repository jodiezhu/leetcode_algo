class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0) #create dummy in order to calcualte to last one
        stack = [0]
        r = 0
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                r = max(r, w*h)
                print("h is",h,"w is",w,"r is",r)
            stack.append(i)
        return r

s=Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
