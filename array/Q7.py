# Merge Overlapping Intervals
# Given a collection of intervals, merge all overlapping intervals.

# For example:

# Given [1,3],[2,6],[8,10],[15,18],

# return [1,6],[8,10],[15,18].

# Make sure the returned intervals are sorted.

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        #import pdb; pdb.set_trace()
        if intervals == []:
            return []
        pivot = intervals.pop(0)
        # till pivot stops growing in size
        pivot_grew = True
        while(pivot_grew):
            pivot_grew = False
            # swallow any intersecting intervals
            for item in intervals:
                if item.start < pivot.start and item.end > pivot.start:
                    pivot.start = item.start
                    pivot_grew = True
                elif item.end > pivot.end and item.start < pivot.end:
                    pivot.end = item.end
                    pivot_grew = True
        lesser = []
        greater = []
        for item in intervals:
            if item.start < pivot.start and item.end < pivot.start:
                lesser.append(item)
            elif item.end > pivot.end and item.start > pivot.end:
                greater.append(item)
            else:  # item sub-interval
                pass
        return self.merge(lesser) + [pivot] + self.merge(greater)