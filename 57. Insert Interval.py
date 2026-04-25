class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        list1 = [intervals[0]]
        for start,end in intervals[1:]:
            last_end = list1[-1][1]
            if start <= last_end:
                list1[-1][1] = max(last_end,end)
            else:
                list1.append([start,end])
        return list1