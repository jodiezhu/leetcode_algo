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


##way2:using Interval class:
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right

s=Solution()
ans=s.insert([Interval(1,3),Interval(6,9)],Interval(0,8))

print(ans[0].end)
    
