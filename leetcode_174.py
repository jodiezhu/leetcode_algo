
class Solution(object):
    def calculateMinimumHP(self, dungeon):
            """
            :type dungeon: List[List[int]]
            :rtype: int
            """
            if not dungeon or len(dungeon) == 0:
                return 0
            
            m = len(dungeon)
            n = len(dungeon[0])
            
            energy = [ [0]*n for _ in range(m) ]

            # energy(i,j) = minimum amount of energy needed to survive dungeon[i][j] AND reach dungeon[m-1][n-1]
            #
            # from (i,j) knight can move to either (i+1,j) or (i,j+1)
            # at (i,j) knight will spend dungeon[i][j] energy, 
            # at (i,j) knight will need min(energy(i+1,j), energy(i,j+1)) to one of the next position
            # 
            # energy needed to survive dungeon(i,j) and move to next position is
            #       min(energy(i+1,j), energy(i+1,j)) - dungeon[i][j]
            #
            # this works in cases where dungeon[i][j] is always negative (-dungeon[i][j]) actually becomes (+abs(dungeon[i][j]))
            # but there're certain booster dungeons, in which case energy(i,j) can become negative or zero, 
            # but minimum energy needed to survive and move on to next is 1
            #
            # so energy(i,j) = max(min( energy(i+1,j), energy(i,j+1) ) - dungeon[i][j] , 1)
            
            
            energy[m-1][n-1] = abs(dungeon[m-1][n-1]) + 1 if dungeon[m-1][n-1] < 0 else 1

            for j in range(n-2,-1,-1): #last row any col
                energy[m-1][j] = max(energy[m-1][j+1] - dungeon[m-1][j], 1)
              
            for i in range(m-2,-1,-1): #last col any row
                energy[i][n-1] = max(energy[i+1][n-1] - dungeon[i][n-1],1)

            for i in range(m-2,-1,-1):
                for j in range(n-2,-1,-1):
                    energy[i][j] = max(  min(energy[i+1][j], energy[i][j+1]) - dungeon[i][j] ,1)

            return energy[0][0]


s=Solution()
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
