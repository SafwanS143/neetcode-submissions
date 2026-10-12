class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        insertedStart = newInterval[0]
        insertedEnd = newInterval[1]
        appended = False
        
        for start, stop in intervals:
            # Before 
            if stop < newInterval[0]:
                inserted.append([start, stop])

            # During
            elif start <= newInterval[1]:
                insertedStart = min(insertedStart, start)
                insertedEnd = max(insertedEnd, stop)

            # After
            else:
                if not appended: inserted.append([insertedStart, insertedEnd]); appended = True
                inserted.append([start, stop])

        if not appended: inserted.append([insertedStart, insertedEnd]); appended = True

        return inserted
