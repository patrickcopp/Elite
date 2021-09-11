class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        # go through all
        # hold current max, compare to start of next
        current_max = intervals[0][1]
        current_min = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > current_max:
                res.append([current_min, current_max])
                current_min = intervals[i][0]
                current_max = intervals[i][1]
                print(current_min,current_max)
            else:
                current_max = max(intervals[i][1], current_max)
        res.append([current_min, current_max])
        return res