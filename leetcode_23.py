import heapq
class Solution(object):
    def MergeFun(self, A): #A:[[1,4,7],[2,3,9,11]]
        ret,heaps=[],[]
        for l in A:
            for item in l:
                heapq.heappush(heaps,item)
        while heaps:
            ret.append(heapq.heappop(heaps))
        return ret


s=Solution()
print(s.MergeFun([[1,4,7],[2,3,9,11]]))
