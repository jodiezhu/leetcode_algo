class MedianFinder(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7

        dq = []    
        for i in range(n): # create a list with nested lists
            dq.append([])
                
        dq[2][0]=1
        dq[2][1]=1
        
        if k==0 or k==n*(n-1)/2: return 1
        if k<0 or k>n*(n-1)/2: return 0
        
        for i in range(3,n+1):
            if k==0: return 1
            for j in range(1,i+1):
                dq[i][j]=dp[i-1][j]+dp[i][j-1]
                if j>=i: dq[i][j]-=dp[i-1][j-i]
                dq[i][j]=(dq[i][j]+MOD)% MOD
        return dq[n][k] 
    
s=MedianFinder()
print(s.kInversePairs(3,1))   
