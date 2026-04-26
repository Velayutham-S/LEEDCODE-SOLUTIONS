class Solution:
    def merge(self, intervals):
        intervals.sort()
        if not intervals:
            return
        list1 = [intervals[0]]
        for start,end in intervals[1:]:
            last_end = list1[-1][1]
            if start <= last_end:
                list1[-1][1] = max(last_end,end)
            else:
                list1.append([start,end])
        return list1