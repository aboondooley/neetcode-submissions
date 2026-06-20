"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        min_room = 1
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        curr = 0
        s,e = 0,0
        while s < len(starts):
            if starts[s] < ends[e]:
                curr+=1
                s+=1
            else:
                curr-=1
                e+=1
            if curr > min_room: min_room = curr
        return min_room

