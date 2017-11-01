
class Solution(object):
    def minTotalDistance(self, grid):
        row_sum = map(sum, grid) #[2,0,1]
        col_sum = map(sum, zip(*grid)) #[1,0,1,0,1]
        
        return self.minTotalDistance1D(row_sum)+self.minTotalDistance1D(col_sum)
    
    def minTotalDistance1D(self,vec):
        i, j = -1, len(vec)
        d = left = right = 0
        print(i,j)
        while i != j:
            if left < right:
                d += left
                i += 1
                left += vec[i]
            else:
                d += right
                j -= 1
                right += vec[j]
            print("d",d,"i",i,"j",j,"left",left,"right",right)
        return d

        

s=Solution()
print(s.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
