class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1]

        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev:
                high = max(intervals[i][1], prev)
                output[-1][1] = high
            
            else:
                output.append(intervals[i])

            prev = output[-1][1]

        return output