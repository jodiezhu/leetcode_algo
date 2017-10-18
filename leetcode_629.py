class MedianFinder(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        if k==0 or k==n*(n-1)/2: return 1
        elif k<0 or k>n*(n-1)/2: return 0

        else:
            dq = [[0]*(k+1) for _ in range(n+1)]    #(n+1) by (k+1) Matrix
                
            dq[2][0]=1
            dq[2][1]=1
        
            for i in range(3,n+1):
                dq[i][0]=1
                for j in range(1,k+1):
                    dq[i][j]=dq[i-1][j]+dq[i][j-1]
                    if j>=i: dq[i][j]-=dq[i-1][j-i]
                    dq[i][j]=(dq[i][j]+MOD)% MOD
        
            return dq[n][k]
         
    
s=MedianFinder()
print(s.kInversePairs(7,2)) 
