class Solution(object):
    def maxrect(self,matrix):
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return 0
        row=len(matrix)
        col=len(matrix[0])
        max_area=0
        heights=[0]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==1:
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.largestRectangleArea(heights)
            max_area=max(max_area,area)
        return max_area

    def largestRectangleArea(self,height):
        height.append(0) #create dummy in order to calcualte to last one
        stack = [0]
        r = 0
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                r = max(r, w*h)
            stack.append(i)
        return r

s=Solution()
print(s.maxrect([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))
