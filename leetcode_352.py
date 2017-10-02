'''
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
'''

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

import heapq

class SummaryRanges(object):

    def __init__(self):
        self.intervals = []
    
    def addNum(self, val):
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        stack = []
        
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals) #
            if not stack:
                stack.append((idx, cur))
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        return list(map(lambda x: x[1], stack))


s=SummaryRanges()
s.addNum(1)
s.addNum(3)
s.addNum(2)
print(s.getIntervals())
