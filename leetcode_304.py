class NumMatrix(object):
    def NumMatrix(self,matrix):
        if not matrix: return 
        self.m=len(matrix)
        self.n=len(matrix[0])

        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i,j,matrix[i][j])
        return self.bit

    def update(self,row , col ,val):
        i=row+1
    
        while i<=self.m:
            j=col+1
            while j<=self.n:
                self.bit[i][j]+=val
                j += j & (-j)          
            i += i & (-i)

    def SumRegion(self,row1,col1,row2,col2):
        return self.getsum(row2,col2)+self.getsum(row1-1,col1-1)-self.getsum(row1-1,col2)-self.getsum(row2,col1-1)
    
    
    def getsum(self,row,col):
        s = 0  
        i = row+1

        while i >0:
            j=col+1
            while j>0:
                s+=self.bit[i][j]
                j-=j & (-j)
            i -= i & (-i)
        return s

freq = NumMatrix()
print(freq.NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]))
print(freq.getsum(4,3))









            
    


        
        
        
        
        
        
        
        
        
        

        
