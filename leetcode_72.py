import sys

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dis = [[0]*(n+1) for _ in range(m+1)]
        
        #initial value:
        for i in range(m+1):
            dis[i][0]=i
               
        for j in range(n+1):
            dis[0][j]=j
            
        for i in range(1,m+1):
            for j in range(1,n+1):
              dis[i][j]=sys.maxsize
              if word1[i-1] == word2[j-1]:
                  dis[i][j]=min(dis[i-1][j],dis[i][j-1])+1
                  dis[i][j]=min(dis[i][j],dis[i-1][j-1])
              else:
                  dis[i][j]=min(dis[i-1][j],dis[i][j-1])+1
                  dis[i][j]=min(dis[i][j],dis[i-1][j-1]+1)                  
        print (dis)
    
s=Solution()
print(s.minDistance("ab","ab"))
