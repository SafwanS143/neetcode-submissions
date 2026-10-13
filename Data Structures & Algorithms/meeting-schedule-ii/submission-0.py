"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        roomsNeed = defaultdict(int)

        for interval in intervals:
            roomsNeed[interval.start] += 1
            roomsNeed[interval.end] -= 1

        runningMax = 0
        curr = 0
        for time in sorted(roomsNeed):
            curr = curr + roomsNeed[time]
            runningMax = max(runningMax, curr)

        return runningMax