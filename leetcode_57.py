class Solution(object):
    def merge_intervals(self,intervals):
        if not intervals: return None
        
        sort_by_low=sorted(intervals,key=lambda x:x[0])
        merge=[]
        
        for item in sort_by_low:
            if not merge:
                merge.append(item)
            else:
                if item[0]<=merge[-1][1]:
                    upper_bound=max(merge[-1][1],item[1])
                    merge[-1]=[merge[-1][0],upper_bound]
                else:
                    merge.append(item)
        return merge
        
        
        
s=Solution()
print(s.merge_intervals ([[1,3],[7,8],[2,5]]))
